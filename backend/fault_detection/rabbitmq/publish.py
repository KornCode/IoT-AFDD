import json
import logging

import aio_pika
from afdd import config

from .setting import RABBITMQ_EXCHANGES

logger = logging.getLogger(__name__)


async def publish_message(exchange_key: str, routing_key: str, payload: dict, headers: dict = None):
    try:
        exchange_conf = RABBITMQ_EXCHANGES[exchange_key]

        connection = await aio_pika.connect_robust(config.RABBITMQ_URL)
        channel = await connection.channel()
        exchange = await channel.declare_exchange(
            exchange_conf["name"],
            type=exchange_conf["type"],
            durable=exchange_conf["durable"],
        )

        message_body = json.dumps(payload).encode()
        message = aio_pika.Message(
            body=message_body,
            content_type="application/json",
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
            headers=headers or {},
        )

        await exchange.publish(message, routing_key=routing_key)

        await channel.close()
        await connection.close()
    except Exception as e:
        logger.error(f"❌ Failed to publish message: {e}")
