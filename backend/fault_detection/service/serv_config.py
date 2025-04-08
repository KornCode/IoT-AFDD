import uuid
from typing import Any, Dict, Optional

from django.core.exceptions import ValidationError
from fault_detection.model_enums import AggregationType, DatapointType, TargetType
from fault_detection.models import FaultDetectionConfig
from fault_detection.repository import repo_config


def create_item(data: dict) -> FaultDetectionConfig:
    target_type = data.get("target_type")
    target_id = data.get("target_id")
    datapoint = data.get("datapoint")
    aggregation = data.get("aggregation", AggregationType.NONE)
    min_value = data.get("min_value")
    max_value = data.get("max_value")
    logic_expression = data.get("logic_expression")
    priority = data.get("priority", 10)
    enabled = data.get("enabled", True)
    alert_repeat_interval_minutes = data.get("alert_repeat_interval_minutes")
    alert_data_silence_threshold_minutes = data.get("alert_data_silence_threshold_minutes")

    if target_type not in TargetType.values:
        raise ValidationError(f"Invalid target type: {target_type}")
    if datapoint not in DatapointType.values:
        raise ValidationError(f"Invalid datapoint type: {datapoint}")
    if aggregation not in AggregationType.values:
        raise ValidationError(f"Invalid aggregation type: {aggregation}")

    try:
        uuid.UUID(str(target_id))
    except ValueError:
        raise ValidationError("Invalid target_id UUID")

    return repo_config.create_row(
        target_type=target_type,
        target_id=target_id,
        datapoint=datapoint,
        aggregation=aggregation,
        min_value=min_value,
        max_value=max_value,
        logic_expression=logic_expression,
        priority=priority,
        enabled=enabled,
        alert_repeat_interval_minutes=alert_repeat_interval_minutes,
        alert_data_silence_threshold_minutes=alert_data_silence_threshold_minutes,
    )


def get_item(config_id: str) -> Optional[FaultDetectionConfig]:
    return repo_config.get_row(config_id)


def update_item(config_id: str, data: Dict[str, Any]) -> Optional[FaultDetectionConfig]:
    return repo_config.update_row(config_id, **data)


def delete_item(config_id: str) -> bool:
    return repo_config.delete_row(config_id)


def get_pagination(query_params: Dict[str, Any]) -> Dict[str, Any]:
    page = int(query_params.get("page", 1))
    per_page = int(query_params.get("per_page", 10))
    datapoint = query_params.get("datapoint")
    target_type = query_params.get("target_type")
    target_id = query_params.get("target_id")

    return repo_config.get_paginated_rows(
        page=page,
        per_page=per_page,
        datapoint=datapoint,
        target_type=target_type,
        target_id=target_id,
    )
