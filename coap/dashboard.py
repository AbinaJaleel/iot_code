
import streamlit as st
import asyncio
import json

from aiocoap import Context, Message, GET


async def get_sensor_data():

    protocol = await Context.create_client_context()

    request = Message(
        code=GET,
        uri="coap://127.0.0.1:5683/sensor"
    )

    response = await protocol.request(request).response

    await protocol.shutdown()

    return json.loads(response.payload.decode())


st.title("CoAP Sensor Dashboard")

if st.button("Get Sensor Data"):

    try:

        data = asyncio.run(get_sensor_data())

        st.metric(
            "Temperature",
            str(data["temperature"]) + " °C"
        )

        st.metric(
            "Humidity",
            str(data["humidity"]) + " %"
        )

        st.success("Data received from CoAP Server!")

    except Exception as e:

        st.error("Server connection failed: " + str(e))
