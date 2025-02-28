import paho.mqtt.client as mqtt
import time
import json
import ssl
import random
import uuid

# Azure IoT Hub Configuration
IOT_HUB_HOSTNAME = "<IOT_HUB_NAME}.azure-devices.net"
DEVICE_ID = "<DEVICE_NAME>"
USERNAME = f"{IOT_HUB_HOSTNAME}/{DEVICE_ID}/?api-version=2021-04-12"
PASSWORD = "<SHARED_ACCESS_SIGNATURE>"
MQTT_PORT = 8883  


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to Azure IoT Hub via MQTT!")
    else:
        print(f"Connection failed with error code {rc}")

# Callback when disconnected from IoT Hub
def on_disconnect(client, userdata, rc):
    print("Disconnected! Attempting reconnect...")
    try:
        client.reconnect()
    except Exception as e:
        print(f"Reconnection failed: {e}")

# Initialize MQTT client
client = mqtt.Client(client_id=DEVICE_ID, protocol=mqtt.MQTTv311)
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set(cert_reqs=ssl.CERT_NONE)  # IoT Hub requires TLS encryption
client.on_connect = on_connect
client.on_disconnect = on_disconnect  # Handles disconnection

# Connect to Azure IoT Hub
client.connect(IOT_HUB_HOSTNAME, MQTT_PORT, 60)
client.loop_start()  # Keeps connection alive and handles automatic reconnection

def generate_sensor_data():
    """Generates a batch of sensor readings with proper temperature-humidity correlation."""
    batch_size = random.randint(3, 4)  # Send 3-4 messages per second
    messages = []

    for _ in range(batch_size):
        timestamp = time.time()  # Epoch timestamp
        event_id = str(uuid.uuid4())  # Unique event ID (optional)
        
        # Temperature-humidity correlation
        base_temp = round(random.uniform(18, 35), 2)
        humidity = round(random.uniform(30, 55) if base_temp > 28 else random.uniform(55, 80), 2)

        data = {
            "deviceId": DEVICE_ID,
            "temperature": base_temp,
            "humidity": humidity,
            "status": "ON",
            "timestamp": timestamp,
            "eventId": event_id  
        }

        messages.append(data)

    return messages

# Cooldown mechanism to prevent consecutive failures
last_failure_time = 0

def simulate_downtime():
    """Introduces occasional downtime, but less frequently and with a cooldown period."""
    global last_failure_time
    current_time = time.time()

    # Ensure at least 15 minutes between failures
    if current_time - last_failure_time < 900:
        return  

    if random.random() < 0.01:  # 1% chance every loop (~every few hours)
        downtime_duration = random.randint(60, 300)  # 1 to 5 minutes
        last_failure_time = time.time()  # Update last failure time
        print(f"SYSTEM FAILURE! No data for {downtime_duration} seconds... Cooling down.")
        time.sleep(downtime_duration)  # Sleep for downtime duration
        print("System Recovered. Resuming data transmission.")

# Publish Sensor Data with Reduced Downtime Frequency
while True:
    simulate_downtime()  # Randomly trigger downtime
    
    sensor_data_batch = generate_sensor_data()
    
    # Publish each message in the batch
    for data in sensor_data_batch:
        message = json.dumps(data)
        print(f"Publishing: {message}")

        result = client.publish(f"devices/{DEVICE_ID}/messages/events/", message, qos=1)

        # Check if publish was successful
        if result.rc != mqtt.MQTT_ERR_SUCCESS:
            print(f"Publish failed: {result.rc}")

    time.sleep(1)  # Keep total rate ~3-4 rows per second
