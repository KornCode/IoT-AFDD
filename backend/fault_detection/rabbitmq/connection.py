import logging

import aio_pika

logger = logging.getLogger(__name__)


class RabbitMQClient:
    def __init__(self, url: str):
        self.url = url
        self.connection = None
        self.channel = None

    async def connect(self):
        self.connection = await aio_pika.connect_robust(self.url)
        self.channel = await self.connection.channel()
        logger.info("[RABBITMQ] ✅ Connection established successfully.")

    async def declare_queue(self, name: str):
        return await self.channel.declare_queue(name, durable=True)

    async def close(self):
        await self.channel.close()
        await self.connection.close()
        logger.info("[RabbitMQ] 🔌 Connection closed successfully.")
