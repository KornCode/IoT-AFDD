RABBITMQ_EXCHANGES = {
    "telemetry.stream": {
        "name": "telemetry.stream",
        "name_dlx": "telemetry.stream.dlx",
        "type": "topic",
        "durable": True,
    },
    "telemetry.event": {
        "name": "telemetry.event",
        "name_dlx": "telemetry.event.dlx",
        "type": "direct",
        "durable": True,
    },
}
