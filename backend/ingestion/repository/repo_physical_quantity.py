from typing import Optional

from django.core.exceptions import ObjectDoesNotExist
from ingestion.models import PhysicalQuantity


def get_row(
    physical_quantity_id: Optional[str] = None, device_id: Optional[str] = None, datapoint: Optional[str] = None
) -> Optional[PhysicalQuantity]:
    try:
        if physical_quantity_id:
            return PhysicalQuantity.objects.get(id=physical_quantity_id)
        elif device_id and datapoint:
            return PhysicalQuantity.objects.get(device__id=device_id, datapoint=datapoint)
    except ObjectDoesNotExist:
        return None
