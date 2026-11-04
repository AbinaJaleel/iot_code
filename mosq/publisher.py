
import paho.mqtt.client as mqtt
import random
import json
import time

# Select broker
broker = "broker.hivemq.com"
# For local Mosquitto use: "localhost"

port = 1883
topic = "iot/sensor/data"

client = mqtt.Client()
client.connect(broker, port, 60)

while True:

    data = {
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 80), 2)
    }

    client.publish(topic, json.dumps(data))

    print("Published:", data)

    time.sleep(5)
