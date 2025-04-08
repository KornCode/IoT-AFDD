import json
import logging
from datetime import datetime

from aio_pika import IncomingMessage
from asgiref.sync import sync_to_async
from asteval import Interpreter
from django.utils import timezone
from ingestion.repository import repo_physical_quantity, repo_raw_data

aeval = Interpreter()
logger = logging.getLogger(__name__)


async def process_and_save(message: IncomingMessage) -> None:
    async with message.process():
        try:
            message_body: dict = json.loads(message.body.decode())
            # logger.info(f"📥 Received telemetry: {message_body}")

            device_id, timestamp, data = (
                message_body.get(key, {} if key == "data" else None) for key in ("device_id", "timestamp", "data")
            )
            if any(value is None for value in (device_id, timestamp, data)):
                raise Exception("'device_id' and 'timestamp', 'data' are required")

            datetime_obj: datetime = timezone.make_aware(datetime.fromtimestamp(timestamp))

            for datapoint, data_value_raw in data.items():
                repo_physical_quantity_result = await sync_to_async(repo_physical_quantity.get_row)(
                    device_id=device_id, datapoint=datapoint
                )
                if not repo_physical_quantity_result:
                    continue

                formula: str = repo_physical_quantity_result.formula or "x"
                aeval.symtable["x"] = data_value_raw

                try:
                    calculated_value = aeval(formula)

                    await sync_to_async(repo_raw_data.insert_row)(
                        timestamp=timestamp,
                        datetime=datetime_obj,
                        device_id=device_id,
                        datapoint=datapoint,
                        value=str(calculated_value),
                    )
                except Exception as e:
                    logger.error(f"❌ Failed to evaluate formula '{formula}' for {datapoint}: {e}")

        except Exception as e:
            logger.error(f"❌ Error handling message: {e}")
