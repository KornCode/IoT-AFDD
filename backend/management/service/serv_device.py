import uuid
from typing import List, Optional

from django.core.exceptions import ValidationError
from management.model_enums import DeviceType
from management.models import Building, Device, Floor, Zone
from management.repository import repo_device


def create_item(data: dict) -> Device:
    zone_id = data.get("zone_id")
    floor_id = data.get("floor_id")
    building_id = data.get("building_id")
    name = data.get("name")
    device_type = data.get("device_type")
    serial_number = data.get("serial_number")
    install_date = data.get("install_date", None)
    metadata = data.get("metadata", {})

    if not name or not device_type or not serial_number:
        raise ValidationError("'name', 'device_type', and 'serial_number' are required")

    if device_type not in DeviceType.values:
        raise ValidationError(f"Invalid device type: {device_type}")

    zone = None
    floor = None
    building = None

    if zone_id:
        try:
            zone = Zone.objects.get(id=zone_id)
        except Zone.DoesNotExist:
            raise ValidationError("Invalid zone_id")

    if floor_id:
        try:
            floor = Floor.objects.get(id=floor_id)
        except Floor.DoesNotExist:
            raise ValidationError("Invalid floor_id")

    if building_id:
        try:
            building = Building.objects.get(id=building_id)
        except Building.DoesNotExist:
            raise ValidationError("Invalid building_id")

    if zone and not floor:
        floor = zone.floor

    if floor and not building:
        building = floor.building

    if zone and not building:
        building = zone.floor.building

    if not building:
        raise ValidationError("Device must belong to at least a zone, floor, or building")

    return repo_device.create_row(
        zone=zone,
        floor=floor,
        building=building,
        name=name,
        device_type=device_type,
        serial_number=serial_number,
        install_date=install_date,
        metadata=metadata,
    )


def get_item(device_id: str) -> Optional[Device]:
    return repo_device.get_row(device_id)


def get_items_by_building(building_id: str) -> List[Device]:
    if not building_id:
        raise ValidationError("building_id is required")

    try:
        building_id = uuid.UUID(str(building_id))
    except ValueError:
        raise ValidationError("Invalid UUID format for building_id")

    return repo_device.get_rows_by_location(building_id=building_id)


def get_items_by_zone(zone_id: str) -> List[Device]:
    if not zone_id:
        raise ValidationError("zone_id is required")

    try:
        zone_id = uuid.UUID(str(zone_id))
    except ValueError:
        raise ValidationError("Invalid UUID format for zone_id")

    return repo_device.get_rows_by_location(zone_id=zone_id)


def update_item(device_id: str, data: dict) -> Optional[Device]:
    return repo_device.update_row(device_id, **data)


def delete_item(device_id: str) -> bool:
    return repo_device.delete_row(device_id)


def get_pagination(query_params: dict) -> dict:
    page = int(query_params.get("page", 1))
    per_page = int(query_params.get("per_page", 10))
    name = query_params.get("name")
    device_type = query_params.get("device_type")
    zone_id = query_params.get("zone_id")
    building_id = query_params.get("building_id")

    return repo_device.get_paginated_rows(
        page=page,
        per_page=per_page,
        name=name,
        device_type=device_type,
        zone_id=zone_id,
        building_id=building_id,
    )
