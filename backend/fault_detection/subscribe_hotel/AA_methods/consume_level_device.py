import json
import logging
from datetime import datetime, timedelta

from aio_pika import IncomingMessage
from asgiref.sync import sync_to_async
from asteval import Interpreter
from django.utils import timezone
from fault_detection.model_enums import AlertMode
from fault_detection.repository import (
    repo_alert,
    repo_config,
    repo_session,
)

logger = logging.getLogger(__name__)
aeval = Interpreter()


def prepare_aeval_context(datapoint: str, data: dict, timestamp: float) -> dict:
    dt = timezone.make_aware(datetime.fromtimestamp(timestamp))
    context = {
        "x": data.get(datapoint),
        "timestamp": timestamp,
        "hour": dt.hour,
        "time_hour": dt.hour,
    }

    # Add all other sensor values to the context
    for key, value in data.items():
        if key != datapoint:
            context[key] = value

    return context


async def detect_and_alert(message: IncomingMessage) -> None:
    async with message.process():
        try:
            message_body: dict = json.loads(message.body.decode())
            # logger.info(f"📥 Received telemetry: {message_body}")

            device_id, timestamp, data = (
                message_body.get(key, {} if key == "data" else None) for key in ("device_id", "timestamp", "data")
            )

            if any(value is None for value in (device_id, timestamp, data)):
                raise Exception("'device_id', 'timestamp', and 'data' are required")

            for datapoint, data_value_raw in data.items():
                # Fetch configs that match device & datapoint
                configs = await sync_to_async(repo_config.get_rows_active_by_target_and_datapoint)(
                    target_id=device_id, datapoint=datapoint
                )

                for config in configs:
                    aeval.symtable.clear()
                    context = prepare_aeval_context(datapoint, data, timestamp)

                    for key, value in context.items():
                        aeval.symtable[key] = value

                    try:
                        triggered: bool = bool(aeval(config.logic_expression or "False"))
                    except Exception as e:
                        logger.error(f"❌ Eval error in logic '{config.logic_expression}': {e}")
                        continue

                    # If not triggered, close any open session
                    if not triggered:
                        session = await sync_to_async(repo_session.get_active_session)(config, device_id, datapoint)
                        if session:
                            await sync_to_async(repo_session.close_session_safe)(session)
                        continue

                    # Fault condition triggered -> open session
                    session_result = await sync_to_async(repo_session.get_or_create_session_safe)(
                        config, device_id, datapoint
                    )

                    # First time triggered -> new alert
                    if session_result.is_new:
                        await sync_to_async(repo_alert.create_alert_safe)(
                            session=session_result.session,
                            config=config,
                            target_id=device_id,
                            datapoint=datapoint,
                            value=data_value_raw,
                            alert_mode=AlertMode.THRESHOLD,
                            is_repeat=False,
                        )
                        # logger.info(f"🚨 New threshold alert created for {datapoint} at {data_value_raw}")
                        continue

                    # Session already exists -> check for repeat
                    last_alert = await sync_to_async(repo_alert.get_last_alert)(session_result.session)
                    now = timezone.now()

                    if config.alert_repeat_interval_minutes:
                        should_repeat: bool = not last_alert or (
                            now - last_alert.alert_time >= timedelta(minutes=config.alert_repeat_interval_minutes)
                        )
                        if should_repeat:
                            await sync_to_async(repo_alert.create_alert_safe)(
                                session=session_result.session,
                                config=config,
                                target_id=device_id,
                                datapoint=datapoint,
                                value=data_value_raw,
                                is_repeat=True,
                                alert_mode=AlertMode.THRESHOLD,
                            )

        except Exception as e:
            logger.error(f"❌ Error handling message: {e}")
