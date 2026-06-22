#  ScreenSync : Cross-Device Intelligent Distributed Screen-Time Management System

##  Overview

**ScreenSync** is a **distributed, real-time, multi-device screen-time management system** that intelligently coordinates usage across devices such as phones, tablets, and laptops.

Unlike traditional screen-time trackers, ScreenSync introduces:

* Cross-device coordination
* Real-time event-driven communication
* Adaptive and context-aware control
* Privacy-preserving intelligence

---

##  Problem Statement

Current screen-time systems:

*  Work per-device (no coordination)
*  Use static limits (no adaptability)
*  Lack real-time synchronization
*  Ignore user context (exam time, location, etc.)

---

##  Proposed Solution

ScreenSync provides a **unified distributed system** where:

* All devices are connected
* Usage is monitored in real-time
* Limits are dynamically adjusted
* Decisions are intelligent and context-aware
---

##  System Architecture

```
Devices (Phone / Tablet / Laptop)
        │
        ▼
   MQTT Broker (Mosquitto)
        │
        ▼
 FastAPI Backend (Coordinator)
        │
        ▼
 PostgreSQL Database
        │
        ▼
 Intelligent Decision Engine
```

---

##  Workflow

1. **Device Registration**

   * Each device registers once and gets a unique ID

2. **Heartbeat Mechanism**

   * Devices periodically send heartbeat signals
   * Backend tracks device status (online/offline)

3. **Real-time Communication (MQTT)**

   * Devices publish usage updates
   * Backend listens instantly (event-driven)

4. **State Synchronization**

   * Backend updates device status and usage

5. **Decision Engine**

   * Applies intelligent rules (rebalancing, context)

6. **Action Enforcement**

   * Updated limits sent to devices

---

##  Key Features / Novelty (Patent-Oriented)

###  Cross-Device Budget Rebalancing Algorithm

* Dynamically redistributes screen-time across devices
* Based on usage patterns and priorities

 Example:

* Tablet → study apps → more time
* Phone → social media → reduced time

 **Novelty**: Adaptive, non-static time allocation

---

### Federated Screen-Time Learning

* Devices do NOT share raw data
* Only model updates are sent
* Backend aggregates insights

✔ Privacy-preserving
✔ Distributed ML approach

 **Patent Potential**: Federated behavioral modeling for digital well-being

---

### Context-Aware Enforcement Engine

* Uses:

  * Time (day/night)
  * Location (home/college)
  * Calendar (exam periods)

 Example:

* Exam week + night → stricter limits

 **Novelty**: Multi-context adaptive restriction system

---

### Conflict Resolution Protocol

* Handles inconsistent states across devices

Uses:

* Timestamp comparison
* Device priority

👉 **Novelty**: Distributed state reconciliation for user control systems

---

###  Emergency Override with Quorum

* User requests extra time
* Requires approval from:

  * Parent device
  * Admin
  * OR 2-of-3 device consensus

👉 Inspired by distributed consensus systems

---

## ⚙️ Tech Stack

### 🧩 Backend

* FastAPI (Python)
* SQLAlchemy (ORM)
* PostgreSQL (Database)

### Real-Time Communication

* MQTT (Mosquitto Broker)
* paho-mqtt (Python client)

### AI / Analytics

* Python
* PyTorch / TensorFlow Lite (future)
* Federated Learning (optional)

### 🔐 Security & Privacy

* OAuth 2.0 (Authentication)
* End-to-End Encryption (planned)
* Device-level anonymization
* Zero-knowledge policy concepts

### 📱 Mobile / Frontend

* Android → Kotlin + UsageStatsManager
* iOS → Swift + Screen Time API
* Tablet → Flutter / Native

---

## 🧠 Distributed System Concepts Used

* Event-driven architecture
* Asynchronous messaging
* Node health monitoring (heartbeat)
* Distributed consensus (quorum)
* State synchronization
* Fault detection (offline detection)

---

## ⚠️ Limitations

1. OS Restrictions (especially iOS APIs)
2. Battery consumption (continuous tracking)
3. Privacy concerns (usage data sensitivity)
4. Network dependency (sync delays possible)

---

## 🔮 Future Scope

* ⌚ Wearable integration (smartwatch monitoring)
* 🏫 School / enterprise deployments
* 🧘 Digital detox recommendations
* 🧠 Mental health prediction models
* 🤖 Fully automated AI-driven control

---

## 🏆 Project Significance

This project goes beyond a basic application and demonstrates:

* Real-world distributed system design
* Scalable architecture using MQTT
* Intelligent decision-making systems
* Strong potential for patent and research

---

## 🧪 How to Run (Quick Setup)

### 1. Start PostgreSQL

 Open pgAdmin

### 2. Start MQTT Broker

```
"E:\Files\Mosquitto\mosquitto.exe" -v
```

### 3. Start Backend

```
cd backend
venv\Scripts\activate
uvicorn app.main:app --reload --port 8001
```

### 4. Open API Docs

```
http://127.0.0.1:8001/docs
```

---

## 🎯 Final Summary

ScreenSync is:

> A **real-time distributed intelligent system** that coordinates and optimizes screen usage across multiple devices using event-driven communication and adaptive decision-making.

---

## 👩‍💻 Author

Shivani Jogiya
(Distributed Computing Project)

---

## Status

✔ Backend complete
✔ MQTT integration done
✔ Real-time sync working
🔄 Algorithm development in progress

---
