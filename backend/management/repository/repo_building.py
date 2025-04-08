import uuid
from typing import Any, Dict, Optional

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from management.models import Building


def create_row(name: str, type: str, address: str, metadata: Optional[Dict[str, Any]] = None) -> Building:
    return Building.objects.create(
        id=uuid.uuid4(),
        name=name,
        type=type,
        address=address,
        metadata=metadata or {},
    )


def get_row(building_id: str) -> Optional[Building]:
    try:
        return Building.objects.get(id=building_id)
    except ObjectDoesNotExist:
        return None


def update_row(building_id: str, **kwargs) -> Optional[Building]:
    building = get_row(building_id)
    if not building:
        return None

    for field, value in kwargs.items():
        if hasattr(building, field):
            setattr(building, field, value)

    building.save()
    return building


def delete_row(building_id: str) -> bool:
    building = get_row(building_id)
    if not building:
        return False

    building.delete()
    return True


def get_paginated_rows(
    page: int = 1,
    per_page: int = 10,
    name: Optional[str] = None,
    type: Optional[str] = None,
) -> Dict[str, Any]:
    qs = Building.objects.all().order_by("-created_at")

    if name:
        qs = qs.filter(name__icontains=name)

    if type:
        qs = qs.filter(type=type)

    paginator = Paginator(qs, per_page)

    try:
        buildings = paginator.page(page)
    except PageNotAnInteger:
        buildings = paginator.page(1)
    except EmptyPage:
        buildings = paginator.page(paginator.num_pages)

    return {
        "results": list(buildings),
        "page": buildings.number,
        "total_pages": paginator.num_pages,
        "total_items": paginator.count,
        "has_next": buildings.has_next(),
        "has_previous": buildings.has_previous(),
    }
