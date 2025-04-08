from datetime import datetime as dt

from ingestion.models import RawData


def insert_row(
    timestamp: int,
    datetime: dt,
    device_id: str,
    datapoint: str,
    value: str,
) -> RawData:
    return RawData.objects.create(
        timestamp=timestamp,
        datetime=datetime,
        device_id=device_id,
        datapoint=datapoint,
        value=value,
    )
