import uuid
from typing import Any, Dict, List, Optional

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import QuerySet
from management.models import Building, Device, Floor, Zone


def create_row(
    zone: Optional[Zone] = None,
    floor: Optional[Floor] = None,
    building: Optional[Building] = None,
    name: Optional[str] = None,
    device_type: Optional[str] = None,
    serial_number: Optional[str] = None,
    install_date: Optional[Any] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Device:
    if zone and not floor:
        floor = zone.floor
    if floor and not building:
        building = floor.building
    if zone and not building:
        building = zone.floor.building

    return Device.objects.create(
        id=uuid.uuid4(),
        zone=zone,
        floor=floor,
        building=building,
        name=name,
        device_type=device_type,
        serial_number=serial_number,
        install_date=install_date,
        metadata=metadata or {},
    )


def get_row(device_id: str) -> Optional[Device]:
    try:
        return Device.objects.get(id=device_id)
    except ObjectDoesNotExist:
        return None


def get_rows_by_location(
    building_id: Optional[str] = None, floor_id: Optional[str] = None, zone_id: Optional[str] = None
) -> List[Device]:
    qs: QuerySet = Device.objects.all().order_by("name")

    if zone_id:
        qs = qs.filter(zone_id=zone_id)
    elif floor_id:
        qs = qs.filter(floor_id=floor_id)
    elif building_id:
        qs = qs.filter(building_id=building_id)
    else:
        raise ValueError("At least one of building_id, floor_id, or zone_id is required")

    return list(qs)


def update_row(device_id: str, **kwargs) -> Optional[Device]:
    device = get_row(device_id)
    if not device:
        return None

    for field, value in kwargs.items():
        if hasattr(device, field):
            setattr(device, field, value)

    device.save()
    return device


def delete_row(device_id: str) -> bool:
    device = get_row(device_id)
    if not device:
        return False

    device.delete()
    return True


def get_paginated_rows(
    page: int = 1,
    per_page: int = 10,
    name: Optional[str] = None,
    device_type: Optional[str] = None,
    zone_id: Optional[str] = None,
    building_id: Optional[str] = None,
) -> Dict[str, Any]:
    qs = Device.objects.all().order_by("-created_at")

    if name:
        qs = qs.filter(name__icontains=name)

    if device_type:
        qs = qs.filter(device_type=device_type)

    if zone_id:
        qs = qs.filter(zone__id=zone_id)

    if building_id:
        qs = qs.filter(building__id=building_id)

    paginator = Paginator(qs, per_page)

    try:
        devices = paginator.page(page)
    except PageNotAnInteger:
        devices = paginator.page(1)
    except EmptyPage:
        devices = paginator.page(paginator.num_pages)

    return {
        "results": list(devices),
        "page": devices.number,
        "total_pages": paginator.num_pages,
        "total_items": paginator.count,
        "has_next": devices.has_next(),
        "has_previous": devices.has_previous(),
    }
