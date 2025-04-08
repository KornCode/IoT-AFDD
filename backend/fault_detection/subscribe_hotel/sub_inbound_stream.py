import logging

from aio_pika.abc import AbstractIncomingMessage
from afdd import config
from fault_detection.rabbitmq.connection import RabbitMQClient
from fault_detection.rabbitmq.setting import RABBITMQ_EXCHANGES
from fault_detection.subscribe_hotel.routing_table import routing_table

logger = logging.getLogger(__name__)

QUEUE_NAME = "telemetry.fault_detection.hotel"

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

            except Exception as e:
                logger.exception(f"❌ Error processing message: {e}")

    await queue.consume(handle_message, no_ack=False)
    logger.info(f"[Consumer] Listening on queue '{QUEUE_NAME}'")
