
import streamlit as st
import requests

url = "https://olwerzkurfutyvmlkpdq.supabase.co/rest/v1/sensor_data?select=*&order=id.desc&limit=1"
key = "sb_publishable_9sos58xD4aUzko3IZMGvBg_51pBySzL"

st.title("MQTT Sensor Dashboard")

if st.button("Refresh Data"):

    response = requests.get(
        url,
        headers={"apikey": key}
    )

    data = response.json()

    if data:
        st.metric("Temperature",
                  str(data[0]["temperature"]) + " °C")

        st.metric("Humidity",
                  str(data[0]["humidity"]) + " %")
    else:
        st.warning("No data available")
