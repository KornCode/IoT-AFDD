from asgiref.sync import sync_to_async
from fault_detection.model_enums import TargetType
from fault_detection.models import FaultDetectionConfig
from fault_detection.rabbitmq.publish import publish_message
from fault_detection.repository import repo_config


async def publish_event_disconnect_alert() -> None:
    config_batches: list[list[FaultDetectionConfig]] = await sync_to_async(
        lambda: list(repo_config.get_rows_active_with_silence_threshold(target_type=TargetType.DEVICE))
    )()

    for batch in config_batches:
        for config in batch:
            routing_key: str = "telemetry.disconnect.device"
            payload: dict = {
                "target_id": config.target_id,
                "datapoint": config.datapoint,
                "threshold_minutes": config.alert_data_silence_threshold_minutes,
            }

            await publish_message(
                exchange_key="telemetry.event",
                routing_key=routing_key,
                payload=payload,
            )
