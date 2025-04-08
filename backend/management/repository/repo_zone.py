import uuid
from typing import Any, Dict, List, Optional

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import QuerySet
from management.models import Floor, Zone


def create_row(floor: Floor, name: str, metadata: Optional[Dict[str, Any]] = None) -> Zone:
    return Zone.objects.create(
        id=uuid.uuid4(),
        floor=floor,
        name=name,
        metadata=metadata or {},
    )


def get_row(zone_id: str) -> Optional[Zone]:
    try:
        return Zone.objects.get(id=zone_id)
    except ObjectDoesNotExist:
        return None


def get_rows_by_floor(floor_id: str) -> List[Zone]:
    if not floor_id:
        raise ValueError("floor_id is required")

    return list(Zone.objects.filter(floor_id=floor_id).order_by("name"))


def update_row(zone_id: str, **kwargs) -> Optional[Zone]:
    zone = get_row(zone_id)
    if not zone:
        return None

    for field, value in kwargs.items():
        if hasattr(zone, field):
            setattr(zone, field, value)

    zone.save()
    return zone


def delete_row(zone_id: str) -> bool:
    zone = get_row(zone_id)
    if not zone:
        return False

    zone.delete()
    return True


def get_paginated_rows(
    page: int = 1,
    per_page: int = 10,
    name: Optional[str] = None,
    floor_id: Optional[str] = None,
) -> Dict[str, Any]:
    qs: QuerySet = Zone.objects.all().order_by("-created_at")

    if name:
        qs = qs.filter(name__icontains=name)

    if floor_id:
        qs = qs.filter(floor__id=floor_id)

    paginator = Paginator(qs, per_page)

    try:
        zones = paginator.page(page)
    except PageNotAnInteger:
        zones = paginator.page(1)
    except EmptyPage:
        zones = paginator.page(paginator.num_pages)

    return {
        "results": list(zones),
        "page": zones.number,
        "total_pages": paginator.num_pages,
        "total_items": paginator.count,
        "has_next": zones.has_next(),
        "has_previous": zones.has_previous(),
    }
