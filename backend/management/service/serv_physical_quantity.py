import uuid
from typing import List, Optional

from management.model_enums import DatapointType
from management.models import Device, PhysicalQuantity
from management.repository import repo_physical_quantity


def create_item(data: dict) -> PhysicalQuantity:
    device = data.get("device")
    datapoint = data.get("datapoint")
    unit = data.get("unit")
    formula = data.get("formula")
    metadata = data.get("metadata", {})

    if not isinstance(device, Device):
        raise TypeError("'device' must be a Device instance")

    if not datapoint or datapoint not in DatapointType.values:
        raise ValueError(f"Invalid or missing 'datapoint': {datapoint}")

    return repo_physical_quantity.create_row(
        device=device,
        datapoint=datapoint,
        unit=unit,
        formula=formula,
        metadata=metadata,
    )


def create_items(data_list: List[dict]) -> List[PhysicalQuantity]:
    for i, data in enumerate(data_list):
        device = data.get("device")
        datapoint = data.get("datapoint")

        if not isinstance(device, Device):
            raise TypeError(f"Item {i}: 'device' must be a Device instance")

        if not datapoint or datapoint not in DatapointType.values:
            raise ValueError(f"Item {i}: Invalid or missing 'datapoint': {datapoint}")

    return repo_physical_quantity.create_rows(data_list)


def get_item(physical_quantity_id: str) -> Optional[PhysicalQuantity]:
    return repo_physical_quantity.get_row(physical_quantity_id)


def get_items_by_device(device_id: str) -> List[PhysicalQuantity]:
    if not device_id:
        raise ValueError("device_id is required")

    try:
        device_id = uuid.UUID(str(device_id))
    except ValueError:
        raise ValueError("Invalid UUID format for device_id")

    return repo_physical_quantity.get_rows_by_device(device_id=device_id)


def update_item(physical_quantity_id: str, data: dict) -> Optional[PhysicalQuantity]:
    return repo_physical_quantity.update_row(physical_quantity_id, **data)


def delete_item(physical_quantity_id: str) -> bool:
    return repo_physical_quantity.delete_row(physical_quantity_id)


def get_pagination(query_params: dict) -> dict:
    page = int(query_params.get("page", 1))
    per_page = int(query_params.get("per_page", 10))
    datapoint = query_params.get("datapoint")
    device_id = query_params.get("device_id")

    return repo_physical_quantity.get_paginated_rows(
        page=page,
        per_page=per_page,
        datapoint=datapoint,
        device_id=device_id,
    )
