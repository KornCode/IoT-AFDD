from typing import Awaitable, Callable

from aio_pika import IncomingMessage
from fault_detection.model_enums import DeviceType

from .AA_methods import consume_level_device


def make_ingest_func(fn: Callable[[IncomingMessage], Awaitable[None]]) -> Callable[[IncomingMessage], Awaitable[None]]:
    async def wrapped(message: IncomingMessage) -> None:
        return await fn(message)

    return wrapped


ROUTING_PREFIX = "telemetry.hotel"

HANDLER_FUNCS = [
    (DeviceType.IAQ.value, consume_level_device.detect_and_alert),
    (DeviceType.PRESENCE.value, consume_level_device.detect_and_alert),
    (DeviceType.ENERGY.value, consume_level_device.detect_and_alert),
]

routing_table = {}
for measurement, fn in HANDLER_FUNCS:
    key = f"{ROUTING_PREFIX}.{measurement}"
    routing_table[key] = make_ingest_func(fn)
    routing_table[f"{key}.requeue"] = make_ingest_func(fn)
