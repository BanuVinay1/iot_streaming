# 📂 Scripts - Utility Queries for IoT Streaming Project

This folder contains useful queries for **monitoring, analytics, and alerting** in the IoT Streaming Pipeline.

## 🔹 Queries Included:
1️⃣ **`stream_analytics_query.sql`**  
   - Used in **Azure Stream Analytics (ASA)** to process IoT sensor data.  
   - Filters **high-temperature events** for further analysis in **ADX/Grafana**.

2️⃣ **`log_analytics_query.kql`**  
   - Used in **Azure Log Analytics** to track real-time IoT event data.  
   - Helps debug if **events are correctly flowing into Log Analytics**.

3️⃣ **`alert_query.kql`**  
   - Monitors **anomalous temperature spikes** and triggers alerts.  
   - Helps in **proactive anomaly detection for IoT devices**.

## 🔹 How to Use:
✅ **Run Stream Analytics Query:**  
   - Copy & paste `stream_analytics_query.sql` into your **ASA job query editor**.

✅ **Track IoT Events in Log Analytics:**  
   - Go to **Log Analytics (Azure Monitor)** and run `log_analytics_query.kql`.

✅ **Trigger Alerts for High Temperature:**  
   - Use `alert_query.kql` in **Azure Monitor Alerts** for **real-time anomaly detection**.

---
