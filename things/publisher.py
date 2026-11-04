

import paho.mqtt.client as mqtt
import random
import json
import time

# ThingsBoard connection
broker = "mqtt.eu.thingsboard.cloud"
port = 1883

# Device access token
token = "YOUR_DEVICE_ACCESS_TOKEN"

# Connection callback
def on_connect(client, userdata, flags, reason_code, properties):
    print("Connection:", reason_code)

    if reason_code == 0:
        print("Connected to ThingsBoard!")
    else:
        print("Connection failed!")

# Create MQTT client
client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.username_pw_set(token)
client.on_connect = on_connect

# Connect to broker
client.connect(broker, port, 60)
client.loop_start()

time.sleep(2)

# Publish sensor data
while True:

    data = {
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 80), 2)
    }

    message = json.dumps(data)

    result = client.publish(
        "v1/devices/me/telemetry",
        message,
        qos=1
    )

    result.wait_for_publish()

    print("Published:", data)

    time.sleep(5)
