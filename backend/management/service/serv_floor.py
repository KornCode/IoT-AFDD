import uuid
from typing import List, Optional

from management.models import Building, Floor
from management.repository import repo_floor


def create_item(data: dict) -> Floor:
    building = data.get("building")
    floor_number = data.get("floor_number")
    name = data.get("name", "")
    metadata = data.get("metadata", {})

    if not isinstance(building, Building):
        raise TypeError("'building' must be a Building instance")

    if not building or floor_number is None:
        raise ValueError("Both 'building' and 'floor_number' are required")

    return repo_floor.create_row(building, floor_number, name, metadata)


def get_item(floor_id: str) -> Optional[Floor]:
    return repo_floor.get_row(floor_id)


def get_items_by_building(building_id: str) -> List[Floor]:
    if not building_id:
        raise ValueError("building_id is required")

    try:
        building_id = uuid.UUID(str(building_id))
    except ValueError:
        raise ValueError("Invalid UUID format for building_id")

    return repo_floor.get_rows_by_building(building_id=building_id)


def update_item(floor_id: str, data: dict) -> Optional[Floor]:
    return repo_floor.update_row(floor_id, **data)


def delete_item(floor_id: str) -> bool:
    return repo_floor.delete_row(floor_id)


def get_pagination(query_params: dict) -> dict:
    page = int(query_params.get("page", 1))
    per_page = int(query_params.get("per_page", 10))
    name = query_params.get("name")
    floor_number = query_params.get("floor_number")
    building_id = query_params.get("building_id")

    return repo_floor.get_paginated_rows(
        page=page,
        per_page=per_page,
        name=name,
        floor_number=floor_number,
        building_id=building_id,
    )
