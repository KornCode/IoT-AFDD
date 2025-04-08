import logging

from fault_detection.models import Device, Floor, Zone

logger = logging.getLogger(__name__)
from fault_detection.models import FaultDetectionConfig


def resolve_hierarchy(config: FaultDetectionConfig, target_id: str) -> dict:
    resolved_fields = {
        "resolved_device_id": None,
        "resolved_zone_id": None,
        "resolved_floor_id": None,
        "resolved_building_id": None,
    }

    try:
        if config.target_type == "device":
            device = Device.objects.select_related("zone__floor__building", "floor__building").get(id=target_id)
            resolved_fields.update(
                {
                    "resolved_device_id": device.id,
                    "resolved_zone_id": device.zone_id,
                    "resolved_floor_id": device.floor_id,
                    "resolved_building_id": device.building_id
                    or (
                        device.floor.building_id
                        if device.floor
                        else device.zone.floor.building_id if device.zone else None
                    ),
                }
            )
        elif config.target_type == "zone":
            zone = Zone.objects.select_related("floor__building").get(id=target_id)
            resolved_fields.update(
                {
                    "resolved_zone_id": zone.id,
                    "resolved_floor_id": zone.floor_id,
                    "resolved_building_id": zone.floor.building_id,
                }
            )
        elif config.target_type == "floor":
            floor = Floor.objects.select_related("building").get(id=target_id)
            resolved_fields.update({"resolved_floor_id": floor.id, "resolved_building_id": floor.building_id})
        elif config.target_type == "building":
            resolved_fields["resolved_building_id"] = target_id
    except Exception as e:
        logger.warning(f"Hierarchy resolution failed for target_id={target_id}, type={config.target_type}: {e}")

    return resolved_fields
