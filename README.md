# ⚡ Automatic Fault Detection and Diagnostic Platform

An Automatic Fault Detection and Diagnostic (AFDD) system built for smart buildings and IoT environments.
It includes a Django-based backend, a telemetry simulator, and a browser-based Supabase-powered frontend.
> 📘 **Note**:
> This project assumes that all telemetry is received in a **standardized format** from a separate IoT integration layer or gateway.
> That upstream service is responsible for:
> - Connecting to physical devices using their native protocols (e.g., Modbus, BACnet, Zigbee, MQTT).
> - Mapping sensor data to a **unified schema** with standardized keys such as `temperature`, `co2`, `power`, etc.
> - Ensuring that the sensor keys match those configured in this system’s database for fault detection logic to evaluate properly.
>
> This design allows this AFDD system to remain agnostic of underlying hardware and focus purely on logic evaluation, session tracking, and alerting.

---

## 📸 Screenshots

### 🧭 Service Overview
![Service Diagram](documents/Service%20Overview.png)

### 🔍 Frontend View
![Frontend Dashboard](documents/Frontend%20View%20Example.png)

### 🧬 Entity-Relationship Diagram
![ER Diagram](documents/ER%20Dragram.png)

📘 [API Reference](documents/API.md)

---

## 📦 Tech Stack

| Layer      | Technology                                 |
|------------|---------------------------------------------|
| Backend    | Django, PostgreSQL, Supabase Realtime       |
| Frontend   | HTML + JavaScript + Supabase SDK            |
| Gateway    | Python, Pandas, Pika (RabbitMQ), threading  |
| Messaging  | RabbitMQ (Topic Exchange)                   |

---

## 🌐 Features

### 🔔 Fault Detection Engine
- Threshold-based fault logic using safe `asteval` expressions.
- Real-time alert generation & session tracking.
- Repeat alerting with customizable intervals.
- Smart expressions like `x > 30 and humidity < 40`.

### 📡 IoT Gateway Simulator
- Streams telemetry from `.csv` files to RabbitMQ.
- Supports temperature, humidity, CO₂, power, presence sensors.
- Simulates random disconnects and publishing intervals.
- Multithreaded for multiple sensors at once.

### 🖥️ Supabase Frontend
- Simple `frontend/index.html` file.
- Uses `@supabase/supabase-js` to **subscribe to alerts in real time**.
- Auto-updates UI when new alerts are inserted to the DB.
- No framework or build tools needed — works in any browser.

---

## 🚀 Getting Started (Docker)

### 1. Clone the repository

```bash
git clone https://github.com/KornCode/IoT-AFDD.git
cd IoT-AFDD
```

### 2. Setup `.env` file

Create `backend/.env` and define:

```env
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# RabbitMQ
RABBITMQ_URL=amqp://guest:guest@rabbitmq:5672/afdd

# Supabase
SUPABASE_DB_URL=
SUPABASE_DB_PREFIX=afdd_
```

Set Supabase connection string inside `frontend/index.html`.

---

### 3. Start the system

```bash
docker-compose up --build
```

### 4. Run backend database migrations

In a new terminal:

```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
```

---

### 5. (Optional) Load Sample Data

A sample seed file is provided at `seed/sample_data.sql` for demo purposes:

---

## 🌐 Access Points

- **Backend API**: http://localhost:5005
- **RabbitMQ Dashboard**: http://localhost:15672
- **Frontend**: Open `frontend/index.html` directly in your browser

---

## 📘 API Reference

- View in GitHub: **[API.md (Postman Markdown Export)](documents/API.md)**
- View in Postman: [https://documenter.getpostman.com/view/5413437/2sB2cVfhbL](https://documenter.getpostman.com/view/5413437/2sB2cVfhbL)

---

## ⚙️ Configuration

Edit `iot_gateway/iot_gateway_mock.py` to simulate:

```python
PUBLISH_INTERVAL_SECONDS = 5
MOCK_DISCONNECT_PROBABILITY = 0.02
DISCONNECT_DURATION_MINUTES = (1, 2)
```

Create alert configs via API or directly in the database:

```json
{
  "target_type": "device",
  "target_id": "...",
  "datapoint": "temperature",
  "logic_expression": "x > 30 and humidity < 40",
  "priority": 5,
  "enabled": true
}
```

---

## 🧠 Example Expressions

These expressions can be used for alert rules:

- `co2 > 1000`
- `temperature > 30 and humidity < 40`
- `hour >= 18 and presence == 0`
- `energy_use_kw > 5 and time_hour < 6`

Variables like `x`, `hour`, `humidity`, `presence`, etc. are dynamically passed into the expression evaluator.

---

## 📚 Documentation

📖 **[Seqeantial Diagrams (GitHub Wiki)](https://github.com/KornCode/IoT-AFDD/wiki/Building-Management-Flow)**
For more insights into service flow, telemetry handling, and alert processing architecture.

---

## 💬 Notes

- `frontend/index.html` uses Supabase’s **`postgres_changes`** to subscribe in real-time.
- It connects directly via `@supabase/supabase-js` without any framework.
- No build tools — just open in browser.

---

## 📡 Telemetry Format

Example message from the simulator:

```json
{
  "device_id": "abc123",
  "timestamp": 1743931783.738,
  "data": {
    "temperature": 25.3,
    "humidity": 47,
    "co2": 510
  }
}
```

---

## 🏗️ Engineering Philosophy

This project was developed with a moderate focus on code quality, scalability, and real-time responsiveness, in alignment with the expectations outlined in the challenge:

#### ✔️ Clean, Modular Code
- The Django backend is organized into three self-contained apps:
  - `management/` – Handles core entities like buildings, devices, floors, and zones.
  - `ingestion/` – Receives and processes real-time telemetry from RabbitMQ.
  - `fault_detection/` – Applies fault logic, session tracking, and generates alerts.
- Each app is **fully decoupled**, with **no circular imports** between them.
- This structure improves **maintainability**, allows **independent testing**, and makes the system **easier to scale or deploy as separate services** if needed.
- Logic is split into clear `repository/`, `service/`, and `route/` layers for clean separation of concerns.
- Uses `async` and `sync_to_async` where appropriate to support non-blocking, real-time processing of high-frequency telemetry streams.


#### ✔️ Thoughtful Backend Design
- Designed around **Supabase Realtime**, **RabbitMQ**, and **PostgreSQL** for fast, reactive telemetry handling.
- Evaluates fault logic using `asteval` for safety and flexibility.
- Session-based tracking avoids redundant alerts.


This foundation is built to be extensible and ready for more sophisticated AFDD logic as the system evolves.

---

## 🧱 Extendability & Future Development

This project serves as a **foundational platform** for real-time IoT fault detection and diagnostics.
It is designed to be **modular, scalable, and easily extensible**.

> 💡 This system lays the groundwork for more advanced AFDD systems and can evolve into a robust solution for **small to medium-sized smart building environments**.
