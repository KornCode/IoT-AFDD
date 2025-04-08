import json
import logging
from datetime import timedelta

from aio_pika import IncomingMessage
from asgiref.sync import sync_to_async
from django.utils import timezone
from fault_detection.model_enums import AlertMode
from fault_detection.repository import (
    repo_alert,
    repo_config,
    repo_raw_data,
    repo_session,
)

logger = logging.getLogger(__name__)


async def detect_and_alert(message: IncomingMessage) -> None:
    async with message.process():
        try:
            message_body: dict = json.loads(message.body.decode())

            target_id: str | None = message_body.get("target_id")
            datapoint: str | None = message_body.get("datapoint")
            threshold_minutes: int | None = message_body.get("threshold_minutes")

            if any(value is None for value in (target_id, datapoint, threshold_minutes)):
                raise Exception("'target_id', 'datapoint', and 'threshold_minutes' are required")

            cutoff_time = timezone.now() - timedelta(minutes=threshold_minutes)

            latest = await sync_to_async(repo_raw_data.get_row_latest_of_device)(
                device_id=target_id,
                datapoint=datapoint,
            )

            if not latest or latest.datetime < cutoff_time:
                logger.warning(f"🚫 No recent data for {datapoint} on {target_id}")

                # Re-fetch full config model
                config = await sync_to_async(repo_config.get_row_by_target_and_datapoint)(
                    target_id=target_id, datapoint=datapoint
                )
                if not config:
                    logger.warning(f"⚠️ Config not found for {target_id}:{datapoint}")
                    return

                session_result = await sync_to_async(repo_session.get_or_create_session_safe)(
                    config=config, target_id=target_id, datapoint=datapoint
                )

                last_alert = await sync_to_async(repo_alert.get_last_alert)(session=session_result.session)
                now = timezone.now()

                should_repeat = not last_alert or (
                    now - last_alert.alert_time >= timedelta(minutes=config.alert_repeat_interval_minutes)
                )

                if should_repeat:
                    await sync_to_async(repo_alert.create_alert_safe)(
                        session=session_result.session,
                        config=config,
                        target_id=target_id,
                        datapoint=datapoint,
                        value=None,
                        alert_mode=AlertMode.DISCONNECT,
                        is_repeat=bool(last_alert),
                    )

        except Exception as e:
            logger.error(f"❌ Error handling message: {e}")
