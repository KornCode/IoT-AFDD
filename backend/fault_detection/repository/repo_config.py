import uuid
from typing import Any, Dict, Generator, List, Optional

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from fault_detection.models import FaultDetectionConfig


def create_row(
    target_type: str,
    target_id: str,
    datapoint: str,
    aggregation: str,
    min_value: Optional[float] = None,
    max_value: Optional[float] = None,
    logic_expression: Optional[str] = None,
    priority: int = 10,
    enabled: bool = True,
    alert_repeat_interval_minutes: Optional[int] = None,
    alert_data_silence_threshold_minutes: Optional[int] = None,
) -> FaultDetectionConfig:
    return FaultDetectionConfig.objects.create(
        id=uuid.uuid4(),
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


def get_row(config_id: str) -> Optional[FaultDetectionConfig]:
    try:
        return FaultDetectionConfig.objects.get(id=config_id)
    except ObjectDoesNotExist:
        return None


def update_row(config_id: str, **kwargs) -> Optional[FaultDetectionConfig]:
    config = get_row(config_id)
    if not config:
        return None

    for field, value in kwargs.items():
        if hasattr(config, field):
            setattr(config, field, value)

    config.save()
    return config


def delete_row(config_id: str) -> bool:
    config = get_row(config_id)
    if not config:
        return False

    config.delete()
    return True


def get_paginated_rows(
    page: int = 1,
    per_page: int = 10,
    datapoint: Optional[str] = None,
    target_type: Optional[str] = None,
    target_id: Optional[str] = None,
) -> Dict[str, Any]:
    qs = FaultDetectionConfig.objects.all().order_by("-created_at")

    if datapoint:
        qs = qs.filter(datapoint=datapoint)

    if target_type:
        qs = qs.filter(target_type=target_type)

    if target_id:
        qs = qs.filter(target_id=target_id)

    paginator = Paginator(qs, per_page)

    try:
        configs = paginator.page(page)
    except PageNotAnInteger:
        configs = paginator.page(1)
    except EmptyPage:
        configs = paginator.page(paginator.num_pages)

    return {
        "results": list(configs),
        "page": configs.number,
        "total_pages": paginator.num_pages,
        "total_items": paginator.count,
        "has_next": configs.has_next(),
        "has_previous": configs.has_previous(),
    }


def get_rows_active_by_target_and_datapoint(target_id: str, datapoint: str) -> List[FaultDetectionConfig]:
    return list(
        FaultDetectionConfig.objects.filter(
            datapoint=datapoint,
            enabled=True,
        )
        .filter(target_id=target_id)
        .order_by("priority")
    )


def get_row_by_target_and_datapoint(target_id: str, datapoint: str) -> Optional[FaultDetectionConfig]:
    return FaultDetectionConfig.objects.filter(target_id=target_id, datapoint=datapoint, enabled=True).first()


def get_rows_active_with_silence_threshold(
    batch_size: int = 100, target_type: Optional[str] = None
) -> Generator[List[FaultDetectionConfig], None, None]:
    qs = FaultDetectionConfig.objects.filter(
        alert_data_silence_threshold_minutes__isnull=False,
        enabled=True,
    ).order_by("id")

    if target_type:
        qs = qs.filter(target_type=target_type)

    total = qs.count()
    for offset in range(0, total, batch_size):
        yield list(qs[offset : offset + batch_size])
