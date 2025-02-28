# 📡 IoT Simulator - MQTT-based Data Streaming to Azure IoT Hub

This Python script simulates an **IoT device sending real-time sensor data** to **Azure IoT Hub via MQTT**.  
It generates **temperature-humidity correlated readings** and includes a **cooldown-based downtime mechanism** to simulate real-world failures.

---

## **🚀 Features**
✅ **Sends real-time temperature & humidity data** using MQTT.  
✅ **Uses TLS encryption** for secure communication with **Azure IoT Hub**.  
✅ **Batching** – Sends 3-4 sensor readings per second.  
✅ **Simulated Downtime** – Introduces occasional failures for realistic behavior.  
✅ **Automatic Reconnection** – Handles **connection loss** with retries.

---

## **🛠️ Setup Instructions**

### **1️⃣ Install Dependencies**
Make sure you have Python installed (`>=3.7`), then install the required dependencies:

```sh
pip install paho-mqtt
