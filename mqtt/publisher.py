
import paho.mqtt.client as mqtt
import random
import json
import time

broker = "broker.hivemq.com"
topic = "iotdemo/abina/sensor"

client = mqtt.Client()
client.connect(broker, 1883)

while True:

    data = {
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 80), 2)
    }

    client.publish(topic, json.dumps(data))

    print("Published:", data)

    time.sleep(5)
