IoT Real-Time Streaming & Analytics Pipeline

📌 Project Overview

This project implements a real-time IoT data streaming pipeline using Azure services to ingest, process, analyze, and visualize IoT sensor data. The system is designed for low-latency processing, real-time alerts, and predictive analytics using machine learning models.

🚀 Architecture
IoT Devices(simulated using python) → Azure IoT Hub → Azure Event Hubs → Azure Stream Analytics → Azure Data Explorer (ADX) → Grafana (Real-time Monitoring)→ Query-Based Triggers (ADX) → Azure Functions (Real-time Alerts)

🔹 Key Components:
Azure IoT Hub – Ingests simulated IoT device data.
Azure Event Hubs – Acts as a message broker for streaming data.
Azure Stream Analytics – Processes and transforms incoming IoT data.
Azure Data Explorer (ADX) – Stores time-series data for querying and analysis.
Grafana – Visualizes real-time IoT telemetry from ADX.
Azure Functions – Triggers real-time alerts based on ADX queries and logs.
Machine Learning (Databricks ML) – Predicts temperature spikes in real-time. (In progress)

🛠️ Setup Instructions
1️⃣ Prerequisites
Azure Subscription
Python 3.x
Azure CLI installed
Terraform (for infrastructure automation)

2️⃣ Deploy Infrastructure
Use Terraform to provision the required Azure resources.

terraform init
terraform apply -auto-approve

3️⃣ Configure IoT Device Simulation
Modify iot_simulator.py to match your IoT Hub settings and run:
python iot_simulator.py

4️⃣ Start Real-Time Processing
Stream Analytics Job:
az stream-analytics job start --name iot-stream --resource-group iot_project_rg
Monitor Data in ADX:
AzureDiagnostics

| where TimeGenerated > ago(10m)
| take 10

Visualize in Grafana:
Add ADX as a data source in Grafana.
Build dashboards to monitor IoT data in real time.

5️⃣ Set Up Real-Time Alerts
Deploy an Azure Function to trigger alerts based on ADX query results.

6️⃣ Real-Time Machine Learning for Anomaly Detection
Implement a real-time ML streaming pipeline in Databricks to predict temperature spikes.

📊 Features & Enhancements
✔️ Real-time IoT Data Ingestion & Processing
✔️ Low-Latency Querying using ADX
✔️ Live Monitoring in Grafana
✔️ Automated Alerts for Anomalies
✔️ Real-time ML-Based Predictions
✔️ Terraform-based Infrastructure Deployment
✔️ Fully Azure-Native Streaming Stack

📖 Future Enhancements
🔹 Edge Computing using Azure IoT Edge for local data processing.
🔹 Advanced AI-Based Anomaly Detection using Databricks ML models.
🔹 CI/CD for automated deployment via Azure DevOps Pipelines.

🤝 Contributing
Feel free to fork this repository, open issues, or submit PRs to improve the pipeline.

📝 License
This project is licensed under the MIT License.

📩 Author: Banu Vinay
🔗 LinkedIn: https://www.linkedin.com/in/banu-vinay-a59703123/
🐙 GitHub: https://github.com/BanuVinay1
