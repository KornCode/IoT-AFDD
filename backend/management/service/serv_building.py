from typing import Optional

from management.model_enums import BuildingType
from management.models import Building
from management.repository import repo_building


def create_item(data: dict) -> Building:
    name = data.get("name")
    type_ = data.get("type")
    address = data.get("address")
    metadata = data.get("metadata", {})

    if type_ not in BuildingType.values:
        raise ValueError(f"Invalid building type: {type_}")

    return repo_building.create_row(name, type_, address, metadata)


def get_item(building_id: str) -> Optional[Building]:
    return repo_building.get_row(building_id)


def update_item(building_id: str, data: dict) -> Optional[Building]:
    return repo_building.update_row(building_id, **data)


def delete_item(building_id: str) -> bool:
    return repo_building.delete_row(building_id)


def get_pagination(query_params: dict) -> dict:
    page = int(query_params.get("page", 1))
    per_page = int(query_params.get("per_page", 10))
    name = query_params.get("name")
    type_ = query_params.get("type")

    return repo_building.get_paginated_rows(
        page=page,
        per_page=per_page,
        name=name,
        type=type_,
    )
