import logging

from aio_pika.abc import AbstractIncomingMessage
from afdd import config
from ingestion.rabbitmq.connection import RabbitMQClient
from ingestion.rabbitmq.publish import publish_message
from ingestion.rabbitmq.setting import RABBITMQ_EXCHANGES
from ingestion.subscribe_hotel.routing_table import routing_table

logger = logging.getLogger(__name__)

QUEUE_NAME = "telemetry.ingestion.hotel"

MAX_RETRIES = 10
PREFETCH_COUNT = 5


async def start_consumer():
    exchange_conf = RABBITMQ_EXCHANGES["telemetry.stream"]

    client = RabbitMQClient(config.RABBITMQ_URL)
    await client.connect()

    channel = client.channel
    await channel.set_qos(prefetch_count=PREFETCH_COUNT)

    queue = await channel.declare_queue(
        QUEUE_NAME,
        durable=True,
        arguments={
            "x-queue-mode": "lazy",
            "x-dead-letter-exchange": exchange_conf["name_dlx"],
        },
    )

    exchange = await channel.declare_exchange(
        exchange_conf["name"],
        type=exchange_conf["type"],
        durable=exchange_conf["durable"],
    )

    for key in routing_table:
        await queue.bind(exchange, routing_key=key)
        # logger.info(f"🔗 Bound exchange '{exchange_conf['name']}' with key '{key}'")

    async def handle_message(message: AbstractIncomingMessage):
        async with message.process(ignore_processed=True):
            try:
                routing_key = message.routing_key
                ingest_function = routing_table.get(routing_key)
                if not ingest_function:
                    # logger.warning(f"⚠️ No ingest_function for routing key: {routing_key}")
                    return await message.nack()

                await ingest_function(message)

            except ValueError as e:
                to_retry, error_message = e.args
                if to_retry is False:
                    return await message.nack(requeue=False)

                headers = message.headers
                if headers is None:
                    return await message.nack(requeue=False)

                retry_attempts = headers.get("x-retry-attempts", 0)
                if retry_attempts >= MAX_RETRIES:
                    return await message.nack(requeue=False)

                retry_attempts += 1

                await publish_message(
                    exchange_key="telemetry.stream",
                    routing_key=message.routing_key.rstrip(".requeue") + ".requeue",
                    payload=message.body,
                    headers=headers.copy(),
                )

            except Exception as e:
                logger.exception(f"❌ Error processing message: {e}")

    await queue.consume(handle_message, no_ack=False)
    logger.info(f"[Consumer] Listening on queue '{QUEUE_NAME}'")
