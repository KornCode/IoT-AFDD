import uuid
from typing import Any, Dict, List, Optional

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import QuerySet
from management.models import Device, PhysicalQuantity


def create_row(
    device: Device,
    datapoint: str,
    unit: Optional[str] = None,
    formula: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> PhysicalQuantity:
    return PhysicalQuantity.objects.create(
        id=uuid.uuid4(),
        device=device,
        datapoint=datapoint,
        unit=unit,
        formula=formula,
        metadata=metadata or {},
    )


def create_rows(data_list: List[Dict[str, Any]]) -> List[PhysicalQuantity]:
    objects = [
        PhysicalQuantity(
            id=uuid.uuid4(),
            device=data["device"],
            datapoint=data["datapoint"],
            unit=data.get("unit"),
            formula=data.get("formula"),
            metadata=data.get("metadata", {}),
        )
        for data in data_list
    ]
    return PhysicalQuantity.objects.bulk_create(objects)


def get_row(physical_quantity_id: str) -> Optional[PhysicalQuantity]:
    try:
        return PhysicalQuantity.objects.get(id=physical_quantity_id)
    except ObjectDoesNotExist:
        return None


def get_rows_by_device(device_id: str) -> List[PhysicalQuantity]:
    return list(PhysicalQuantity.objects.filter(device_id=device_id).order_by("datapoint"))


def update_row(physical_quantity_id: str, **kwargs) -> Optional[PhysicalQuantity]:
    pq = get_row(physical_quantity_id)
    if not pq:
        return None

    for field, value in kwargs.items():
        if hasattr(pq, field):
            setattr(pq, field, value)

    pq.save()
    return pq


def delete_row(physical_quantity_id: str) -> bool:
    pq = get_row(physical_quantity_id)
    if not pq:
        return False

    pq.delete()
    return True


def get_paginated_rows(
    page: int = 1, per_page: int = 10, datapoint: Optional[str] = None, device_id: Optional[str] = None
) -> Dict[str, Any]:
    qs: QuerySet = PhysicalQuantity.objects.all().order_by("-created_at")

    if datapoint:
        qs = qs.filter(datapoint=datapoint)

    if device_id:
        qs = qs.filter(device__id=device_id)

    paginator = Paginator(qs, per_page)

    try:
        pqs = paginator.page(page)
    except PageNotAnInteger:
        pqs = paginator.page(1)
    except EmptyPage:
        pqs = paginator.page(paginator.num_pages)

    return {
        "results": list(pqs),
        "page": pqs.number,
        "total_pages": paginator.num_pages,
        "total_items": paginator.count,
        "has_next": pqs.has_next(),
        "has_previous": pqs.has_previous(),
    }
