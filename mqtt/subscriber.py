
import paho.mqtt.client as mqtt
import requests
import json

broker = "broker.hivemq.com"
topic = "iotdemo/abina/sensor"

url = "https://olwerzkurfutyvmlkpdq.supabase.co/rest/v1/sensor_data?select=*&order=id.desc&limit=1"
key = "sb_publishable_9sos58xD4aUzko3IZMGvBg_51pBySzL"

def on_message(client, userdata, msg):

    data = json.loads(msg.payload.decode())

    print("Received:", data)

    response = requests.post(
        url,
        json=data,
        headers={
            "apikey": key,
            "Authorization": "Bearer " + key,
            "Content-Type": "application/json"
        }
    )

    print("Supabase status:", response.status_code)

client = mqtt.Client()
client.on_message = on_message

client.connect(broker, 1883)
client.subscribe(topic)

print("Waiting for MQTT data...")

client.loop_forever()
