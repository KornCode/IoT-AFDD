# ⚡ Automatic Fault Detection and Diagnostic Platform

An Automatic Fault Detection and Diagnostic (AFDD) system built for smart buildings and IoT environments.
It includes a Django-based backend, a telemetry simulator, and a browser-based Supabase-powered frontend.

> 📘 **Note**
> This project assumes all telemetry is received in a **standardized format** from an external IoT integration layer.
> That upstream service is responsible for:
> - Connecting to physical devices (e.g., Modbus, BACnet, Zigbee, MQTT).
> - Mapping sensor data to a **unified schema** with standardized keys like `temperature`, `co2`, `power`, etc.
> - Ensuring keys match those configured in this system’s database.
>
> This lets the AFDD platform stay hardware-agnostic, focusing on logic evaluation, alerting, and session tracking.

---

## 📸 Screenshots

### 🧭 Service Overview
![Service Diagram](documents/Service%20Overview.png)

### 🔍 Frontend View
![Frontend Dashboard](documents/Frontend%20View%20Example.png)

### 🧬 Entity-Relationship Diagram
![ER Diagram](documents/ER%20Dragram.png)

📘 [API Reference (Markdown)](documents/API.md) • [API (Postman)](https://documenter.getpostman.com/view/5413437/2sB2cVfhbL)

---

## 📦 Tech Stack

| Layer      | Technology                                 |
|------------|---------------------------------------------|
| Backend    | Django, PostgreSQL, Supabase Realtime       |
| Frontend   | HTML + JS + Supabase SDK                    |
| Gateway    | Python, Pandas, Pika (RabbitMQ)             |
| Messaging  | RabbitMQ (Topic Exchange)                   |

---

## 🌐 Features

### 🔔 Fault Detection Engine
- Evaluates safe `asteval` expressions (e.g. `x > 30 and humidity < 40`).
- Real-time alerting with session tracking to suppress duplicates.
- Repeat alerting with configurable intervals.

### 📡 IoT Gateway Simulator
- Multithreaded telemetry publisher using `.csv` sample files.
- Simulates IAQ, power, and presence data.
- Supports configurable publishing rate and random disconnects.

### 🖥️ Supabase Frontend
- Minimal `frontend/index.html` using Supabase WebSocket.
- Auto-updates on DB insert via `postgres_changes`.
- Works in any browser — no React, no build step.

---

## 🚀 Getting Started (Docker)

### 1. Clone the Repository

```bash
git clone https://github.com/KornCode/IoT-AFDD.git
cd IoT-AFDD
```

### 2. Configure Environment

Create `backend/.env` with:

```env
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

RABBITMQ_URL=amqp://guest:guest@rabbitmq:5672/afdd

SUPABASE_DB_URL=
SUPABASE_DB_PREFIX=afdd_
```

Set Supabase connection string in `frontend/index.html`.

---

### 3. Start the System

```bash
docker-compose up --build
```

### 4. Apply Database Migrations

```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
```

### 5. (Optional) Load Sample Data

A sample SQL seed file is available at:

```bash
seed/sample_data.sql
```

---

## 🌐 Access Points

- **Backend API**: http://localhost:5005
- **RabbitMQ Dashboard**: http://localhost:15672
- **Frontend**: Open `frontend/index.html` directly in your browser

---

## 📘 API Reference

- GitHub: [documents/API.md](documents/API.md)
- Postman: [https://documenter.getpostman.com/view/5413437/2sB2cVfhbL](https://documenter.getpostman.com/view/5413437/2sB2cVfhbL)

---

## ⚙️ Configuration

Edit `iot_gateway/iot_gateway_mock.py`:

```python
PUBLISH_INTERVAL_SECONDS = 5
MOCK_DISCONNECT_PROBABILITY = 0.02
DISCONNECT_DURATION_MINUTES = (1, 2)
```

Example alert config:

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

- `co2 > 1000`
- `temperature > 30 and humidity < 40`
- `hour >= 18 and presence == 0`
- `energy_use_kw > 5 and time_hour < 6`

All expression variables are injected dynamically at runtime.

---

## 📚 Documentation

📖 **[Sequential Diagrams (GitHub Wiki)](https://github.com/KornCode/IoT-AFDD/wiki/Building-Management-Flow)**

---

## 💬 Notes

- `frontend/index.html` uses Supabase’s **`postgres_changes`** to subscribe in real-time.
- No framework required — just open in your browser.

---

## 📡 Telemetry Format

Example incoming message:

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

### ✔️ Clean, Modular Code

- Django backend is organized into 3 apps:
  - `management/` – Core data: devices, buildings, floors, zones.
  - `ingestion/` – RabbitMQ message consumption.
  - `fault_detection/` – Logic evaluation and alert generation.
- Apps are fully **decoupled** with **no circular imports**.
- Clear architecture using `repository/`, `service/`, and `route/` layers.
- Real-time message processing via `async`/`sync_to_async`.

### ✔️ Thoughtful Backend Design

- Built with Supabase Realtime, RabbitMQ, and PostgreSQL for responsive telemetry handling.
- Fault logic is evaluated using `asteval` for safety and flexibility.
- Session-based tracking prevents duplicate alert spam.
- Architecture is extensible to zone-, floor-, or building-level evaluations.

---

## 🧱 Future Possibilities

This project serves as a **foundation for small to medium-sized smart building systems**.
It is modular, scalable, and extensible — enabling future features such as:

- Aggregated logic (zone/floor/building)
- Anomaly detection models
- Role-based dashboards and analytics
