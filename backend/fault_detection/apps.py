import asyncio
import logging
import threading

from django.apps import AppConfig
from django.db import connection

logger = logging.getLogger(__name__)


class FaultDetectionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fault_detection"

    def ready(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
        logger.info("[SUPABASE] ✅ Connection established successfully.")

        from fault_detection.subscribe_disconnect.sub_inbound_event import (
            start_consumer as start_consumer_disconnect,
        )
        from fault_detection.subscribe_hotel.sub_inbound_stream import (
            start_consumer as start_consumer_hotel,
        )

        def start_event_loop():
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

                loop.run_until_complete(
                    asyncio.gather(
                        start_consumer_hotel(),
                        start_consumer_disconnect(),
                    )
                )
                loop.run_forever()
            except asyncio.CancelledError:
                logger.warning("🔁 Event loop cancelled (autoreload?) — shutting down consumer thread")
            except Exception as e:
                logger.exception("❌ Failed to start RabbitMQ consumer event loop")

        thread = threading.Thread(
            target=start_event_loop,
            name="RabbitMQConsumerThread",
            daemon=True,
        )
        thread.start()
