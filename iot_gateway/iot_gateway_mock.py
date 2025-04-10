import os
import time
import json
import logging
import random
import pandas as pd
import asyncio
import aio_pika
from pathlib import Path
from datetime import datetime

# ─── CONFIGURABLE SIMULATION SETTINGS ───────────────────────────────────────────

PUBLISH_INTERVAL_SECONDS = 5  # How often to publish each data point
MOCK_DISCONNECT_PROBABILITY = 0.02  # Probability of simulating a disconnect (0.0 - 1.0)
DISCONNECT_DURATION_MINUTES = (3.0, 5.0)  # Disconnect duration range in minutes

# ────────────────────────────────────────────────────────────────────────────────

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

RABBITMQ_URL = "amqp://guest:guest@rabbitmq:5672/afdd"
EXCHANGE_NAME = "telemetry.stream"
EXCHANGE_TYPE = "topic"

DEVICE_IDS = {
    "sample_power_meter_data.csv": [
        "f8b315f5-195b-4ff4-b773-81542c739ede",
        "9d821104-e0ae-46c4-8eee-b9c041035425",
        "6c250940-9662-4378-ade9-cc6f2b813ba4",
        "6fb2ed4d-11bc-4dc5-8080-2df71346446a",
        "45cc791c-eec0-412c-9250-4bb1c425e343",
    ],
    "sample_iaq_data_Room101.csv": "6c731696-ca4a-4167-9ac4-8bf31fec7e57",
    "sample_iaq_data_Room102.csv": "86c68733-4da4-4d95-b0ba-26eed4880e98",
    "sample_iaq_data_Room103.csv": "6c731696-ca4a-4167-9ac4-8bf31fec7e57",
    "sample_presence_sensor_data_Room101.csv": "ec5c8170-c97a-483a-b2be-979f7a960780",
    "sample_presence_sensor_data_Room102.csv": "52e1d349-844e-4167-8901-fdc46fd3e70a",
    "sample_presence_sensor_data_Room103.csv": "6f15fe69-e63c-451e-80e4-6bb647827666",
}

DATA_DIR = Path(__file__).parent / "sample_data"
dataframes = {}
for file in DEVICE_IDS:
    path = os.path.join(DATA_DIR, file)
    try:
        dataframes[file] = pd.read_csv(path)
        logger.info(f"✅ Loaded {file} ({len(dataframes[file])} rows)")
    except Exception as e:
        logger.error(f"❌ Failed to load {file}: {e}")


async def send_data(file_name, device_ids, measurement):
    try:
        connection = await aio_pika.connect_robust(RABBITMQ_URL)
        channel = await connection.channel()
        exchange = await channel.declare_exchange(EXCHANGE_NAME, EXCHANGE_TYPE, durable=True)
        logger.info(f"📡 Connected to RabbitMQ and declared exchange: {EXCHANGE_NAME}")
    except Exception as e:
        logger.error(f"❌ RabbitMQ connection failed: {e}")
        return

    df = dataframes[file_name]
    index = 0
    lost_counter = 0
    lost_duration = 0
    routing_key = f"{measurement}"

    while True:
        if lost_duration > 0:
            lost_counter += 1
            if lost_counter >= lost_duration:
                lost_duration = 0
                lost_counter = 0
            else:
                await asyncio.sleep(PUBLISH_INTERVAL_SECONDS)
                continue

        if random.random() < MOCK_DISCONNECT_PROBABILITY:
            lost_duration = int(random.uniform(*DISCONNECT_DURATION_MINUTES) * 60 / PUBLISH_INTERVAL_SECONDS)
            logger.warning(f"⚠️ Simulating message loss for {file_name} ({lost_duration * PUBLISH_INTERVAL_SECONDS}s)")
            await asyncio.sleep(PUBLISH_INTERVAL_SECONDS)
            continue

        row = df.iloc[index % len(df)]

        if isinstance(device_ids, list):
            for col, device_id in zip(df.columns, device_ids):
                if col.lower() == "datetime":
                    continue
                payload = {"device_id": device_id, "timestamp": datetime.utcnow().timestamp(), "value": row[col]}
                await exchange.publish(aio_pika.Message(body=json.dumps(payload).encode()), routing_key=routing_key)
                logger.info(f"📤 Sent to [{routing_key}] for device {device_id}")
        else:
            row_data = row.to_dict()
            row_data.pop("datetime", None)
            payload = {"device_id": device_ids, "timestamp": datetime.utcnow().timestamp(), "data": row_data}
            await exchange.publish(aio_pika.Message(body=json.dumps(payload).encode()), routing_key=routing_key)
            logger.info(f"📤 Sent to [{routing_key}] for device {device_ids}")

        index += 1
        await asyncio.sleep(PUBLISH_INTERVAL_SECONDS)


async def main():
    tasks = [
        send_data("sample_power_meter_data.csv", DEVICE_IDS["sample_power_meter_data.csv"], "telemetry.hotel.power"),
        send_data("sample_iaq_data_Room101.csv", DEVICE_IDS["sample_iaq_data_Room101.csv"], "telemetry.hotel.iaq"),
        send_data("sample_iaq_data_Room102.csv", DEVICE_IDS["sample_iaq_data_Room102.csv"], "telemetry.hotel.iaq"),
        send_data("sample_iaq_data_Room103.csv", DEVICE_IDS["sample_iaq_data_Room103.csv"], "telemetry.hotel.iaq"),
        send_data(
            "sample_presence_sensor_data_Room101.csv",
            DEVICE_IDS["sample_presence_sensor_data_Room101.csv"],
            "telemetry.hotel.presence",
        ),
        send_data(
            "sample_presence_sensor_data_Room102.csv",
            DEVICE_IDS["sample_presence_sensor_data_Room102.csv"],
            "telemetry.hotel.presence",
        ),
        send_data(
            "sample_presence_sensor_data_Room103.csv",
            DEVICE_IDS["sample_presence_sensor_data_Room103.csv"],
            "telemetry.hotel.presence",
        ),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
