import uuid
from typing import Any, Dict, List, Optional

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import QuerySet
from management.models import Building, Floor


def create_row(
    building: Building,
    floor_number: int,
    name: str = "",
    metadata: Optional[Dict[str, Any]] = None,
) -> Floor:
    return Floor.objects.create(
        id=uuid.uuid4(),
        building=building,
        floor_number=floor_number,
        name=name,
        metadata=metadata or {},
    )


def get_row(floor_id: str) -> Optional[Floor]:
    try:
        return Floor.objects.get(id=floor_id)
    except ObjectDoesNotExist:
        return None


def get_rows_by_building(building_id: str) -> List[Floor]:
    return list(Floor.objects.filter(building_id=building_id).order_by("floor_number"))


def update_row(floor_id: str, **kwargs) -> Optional[Floor]:
    floor = get_row(floor_id)
    if not floor:
        return None

    for field, value in kwargs.items():
        if hasattr(floor, field):
            setattr(floor, field, value)

    floor.save()
    return floor


def delete_row(floor_id: str) -> bool:
    floor = get_row(floor_id)
    if not floor:
        return False

    floor.delete()
    return True


def get_paginated_rows(
    page: int = 1,
    per_page: int = 10,
    name: Optional[str] = None,
    floor_number: Optional[int] = None,
    building_id: Optional[str] = None,
) -> Dict[str, Any]:
    qs: QuerySet = Floor.objects.all().order_by("-created_at")

    if name:
        qs = qs.filter(name__icontains=name)

    if floor_number is not None:
        qs = qs.filter(floor_number=floor_number)

    if building_id:
        qs = qs.filter(building_id=building_id)

    paginator = Paginator(qs, per_page)

    try:
        floors = paginator.page(page)
    except PageNotAnInteger:
        floors = paginator.page(1)
    except EmptyPage:
        floors = paginator.page(paginator.num_pages)

    return {
        "results": list(floors),
        "page": floors.number,
        "total_pages": paginator.num_pages,
        "total_items": paginator.count,
        "has_next": floors.has_next(),
        "has_previous": floors.has_previous(),
    }
