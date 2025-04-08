import uuid
from typing import List, Optional

from management.models import Floor, Zone
from management.repository import repo_zone


def create_item(data: dict) -> Zone:
    floor = data.get("floor")
    name = data.get("name")
    metadata = data.get("metadata", {})

    if not isinstance(floor, Floor):
        raise TypeError("'floor' must be a Floor instance")

    if not name:
        raise ValueError("'name' is required")

    return repo_zone.create_row(floor, name, metadata)


def get_item(zone_id: str) -> Optional[Zone]:
    return repo_zone.get_row(zone_id)


def get_items_by_floor(floor_id: str) -> List[Zone]:
    if not floor_id:
        raise ValueError("floor_id is required")

    try:
        floor_id = uuid.UUID(str(floor_id))
    except ValueError:
        raise ValueError("Invalid UUID format for floor_id")

    return repo_zone.get_rows_by_floor(floor_id=floor_id)


def update_item(zone_id: str, data: dict) -> Optional[Zone]:
    return repo_zone.update_row(zone_id, **data)


def delete_item(zone_id: str) -> bool:
    return repo_zone.delete_row(zone_id)


def get_pagination(query_params: dict) -> dict:
    page = int(query_params.get("page", 1))
    per_page = int(query_params.get("per_page", 10))
    name = query_params.get("name")
    floor_id = query_params.get("floor_id")

    return repo_zone.get_paginated_rows(
        page=page,
        per_page=per_page,
        name=name,
        floor_id=floor_id,
    )
