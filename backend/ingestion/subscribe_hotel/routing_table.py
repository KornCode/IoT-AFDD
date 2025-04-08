from typing import Awaitable, Callable

from aio_pika import IncomingMessage
from ingestion.model_enums import DeviceType

from .AA_methods import consume_telemetry


def make_ingest_func(fn: Callable[[IncomingMessage], Awaitable[None]]) -> Callable[[IncomingMessage], Awaitable[None]]:
    async def wrapped(message: IncomingMessage) -> None:
        return await fn(message)

    return wrapped


ROUTING_PREFIX = "telemetry.hotel"

HANDLER_FUNCS = [
    (DeviceType.IAQ.value, consume_telemetry.process_and_save),
    (DeviceType.PRESENCE.value, consume_telemetry.process_and_save),
    (DeviceType.ENERGY.value, consume_telemetry.process_and_save),
]

routing_table = {}
for measurement, fn in HANDLER_FUNCS:
    key = f"{ROUTING_PREFIX}.{measurement}"
    routing_table[key] = make_ingest_func(fn)
    routing_table[f"{key}.requeue"] = make_ingest_func(fn)
