from typing import Optional

from fault_detection.models import RawData


def get_row_latest_of_device(device_id: str, datapoint: str) -> Optional[RawData]:
    return RawData.objects.filter(device_id=device_id, datapoint=datapoint).order_by("-datetime").first()
