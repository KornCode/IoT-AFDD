import uuid
from typing import List

from django.core.exceptions import ValidationError
from fault_detection.model_enums import TargetType
from fault_detection.models import FaultAlert
from fault_detection.repository import repo_alert


def get_items_active_alert_by_building(target_id: str) -> List[FaultAlert]:
    if not target_id:
        raise ValidationError("target_id is required for building-level alert query")

    try:
        uuid.UUID(str(target_id))
    except ValueError:
        raise ValidationError("Invalid target_id UUID")

    return repo_alert.get_rows_active_alert(target_type=TargetType.BUILDING, target_id=target_id)


def get_items_active_alert_by_floor(target_id: str) -> List[FaultAlert]:
    if not target_id:
        raise ValidationError("target_id is required for floor-level alert query")

    try:
        uuid.UUID(str(target_id))
    except ValueError:
        raise ValidationError("Invalid target_id UUID")

    return repo_alert.get_rows_active_alert(target_type=TargetType.FLOOR, target_id=target_id)


def get_items_active_alert_by_zone(target_id: str) -> List[FaultAlert]:
    if not target_id:
        raise ValidationError("target_id is required for zone-level alert query")

    try:
        uuid.UUID(str(target_id))
    except ValueError:
        raise ValidationError("Invalid target_id UUID")

    return repo_alert.get_rows_active_alert(target_type=TargetType.ZONE, target_id=target_id)


def get_items_active_alert_by_device(target_id: str) -> List[FaultAlert]:
    if not target_id:
        raise ValidationError("target_id is required for device-level alert query")

    try:
        uuid.UUID(str(target_id))
    except ValueError:
        raise ValidationError("Invalid target_id UUID")

    return repo_alert.get_rows_active_alert(target_type=TargetType.DEVICE, target_id=target_id)


def acknowledge_item(alert_id: str, acknowledged_by: str, include_older: bool = True) -> List[FaultAlert]:
    if not acknowledged_by:
        raise ValidationError("acknowledged_by is required")

    try:
        uuid.UUID(str(alert_id))
    except ValueError:
        raise ValidationError("Invalid alert_id UUID")

    try:
        return repo_alert.acknowledge_alert(
            alert_id=alert_id,
            acknowledged_by=acknowledged_by,
            include_older=include_older,
        )
    except ValueError as e:
        raise ValidationError(str(e))
