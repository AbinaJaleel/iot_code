
import requests
import random
import time

url = "https://olwerzkurfutyvmlkpdq.supabase.co/rest/v1/sensor_data"
key = "sb_publishable_9sos58xD4aUzko3IZMGvBg_51pBySzL"
headers = {
    "apikey": key,
    "Authorization": "Bearer " + key,
    "Content-Type": "application/json"
}

while True:

    data = {
        "temperature": random.randint(20, 35),
        "humidity": random.randint(40, 80)
    }

    response = requests.post(url, json=data, headers=headers)

    print("Sending:", data)
    print("Status:", response.status_code)
    print("Response:", response.text)

    time.sleep(5)

