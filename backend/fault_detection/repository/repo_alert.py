import logging
from typing import List, Optional

from django.db import transaction
from django.db.models import Q
from django.utils import timezone
from fault_detection.model_enums import TargetType
from fault_detection.models import FaultAlert, FaultDetectionConfig, FaultSession

logger = logging.getLogger(__name__)
from .AA_methods import method_alert


def get_last_alert(session: FaultSession) -> Optional[FaultAlert]:
    return FaultAlert.objects.filter(session=session).order_by("-alert_time").first()


@transaction.atomic
def create_alert_safe(
    session: FaultSession,
    config: FaultDetectionConfig,
    target_id: str,
    datapoint: str,
    value: Optional[float],
    alert_mode: str,
    is_repeat: bool = False,
) -> FaultAlert:
    metadata = {
        "is_repeat": is_repeat,
    }

    resolved_fields = method_alert.resolve_hierarchy(config=config, target_id=target_id)
    return FaultAlert.objects.create(
        session=session,
        config=config,
        target_type=config.target_type,
        target_id=target_id,
        datapoint=datapoint,
        value=value,
        metadata=metadata,
        alert_time=timezone.now(),
        alert_mode=alert_mode,
        **resolved_fields,
    )


def get_rows_active_alert(target_type: TargetType, target_id: str) -> List[FaultAlert]:
    if target_type == TargetType.BUILDING:
        field = "resolved_building_id"
    elif target_type == TargetType.FLOOR:
        field = "resolved_floor_id"
    elif target_type == TargetType.ZONE:
        field = "resolved_zone_id"
    elif target_type == TargetType.DEVICE:
        field = "resolved_device_id"
    else:
        raise ValueError(f"Unsupported target_type: {target_type}")

    filter_kwargs = {
        "resolved_at__isnull": True,
        field: target_id,
    }

    qs = FaultAlert.objects.filter(**filter_kwargs)
    return list(qs.order_by("-alert_time"))


@transaction.atomic
def acknowledge_alert(alert_id: str, acknowledged_by: str, include_older: bool = True) -> List[FaultAlert]:
    try:
        alert: FaultAlert = FaultAlert.objects.get(id=alert_id)
        if alert.status != "active":
            raise ValueError("Only active alerts can be acknowledged")

        now = timezone.now()

        # Acknowledge the selected alert
        alert.status = "acknowledged"
        alert.acknowledged_at = now
        alert.acknowledged_by = acknowledged_by
        alert.save()

        updated_alerts: List[FaultAlert] = [alert]

        if include_older:
            # Acknowledge older active alerts with the same target
            older_alerts = FaultAlert.objects.filter(
                Q(target_type=alert.target_type),
                Q(target_id=alert.target_id),
                Q(status="active"),
                Q(alert_time__lt=alert.alert_time),
            ).exclude(id=alert.id)

            older_alerts.update(
                status="acknowledged",
                acknowledged_at=now,
                acknowledged_by=acknowledged_by,
            )

            updated_alerts.extend(older_alerts)

        return updated_alerts

    except FaultAlert.DoesNotExist:
        raise ValueError("Alert not found")
