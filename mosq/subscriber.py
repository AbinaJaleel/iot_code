
import paho.mqtt.client as mqtt
import json

# Select broker
broker = "broker.hivemq.com"
# For local Mosquitto use: "localhost"

port = 1883
topic = "iot/sensor/data"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(topic)

def on_message(client, userdata, msg):

    data = json.loads(msg.payload.decode())

    print("\nReceived Sensor Data")
    print("Temperature:", data["temperature"], "°C")
    print("Humidity:", data["humidity"], "%")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)

print("Waiting for sensor data...")

client.loop_forever()
