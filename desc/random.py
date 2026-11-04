
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay

# Dashboard
st.title("Room Occupancy Detection Dashboard")
st.write("Occupancy Prediction using Decision Tree")
st.divider()

# Read dataset
data = pd.read_csv("datatraining.txt")
df = pd.DataFrame(data)

st.subheader("Dataset")
st.write("Total Rows:", len(df))
st.dataframe(df.head())

# Features and target
features = ["Temperature", "Humidity", "Light", "CO2"]
target = "Occupancy"

df = df[features + [target]]

# Preprocessing
df = df.dropna()

st.subheader("Statistical Analysis")
st.dataframe(df[features].describe())

# Split data
x = df[features]
y = df[target]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = DecisionTreeClassifier(random_state=42)

model.fit(x_train, y_train)

# Prediction
pred = model.predict(x_test)

# Evaluation
accuracy = accuracy_score(y_test, pred)

st.subheader("Model Accuracy")
st.metric("Accuracy", f"{accuracy*100:.2f}%")

# Confusion Matrix
st.subheader("Confusion Matrix")

fig, ax = plt.subplots()

ConfusionMatrixDisplay.from_predictions(
    y_test, pred,
    display_labels=["Not Occupied", "Occupied"],
    ax=ax
)

st.pyplot(fig)

# User input
st.subheader("Enter Sensor Values")

temp = st.number_input("Temperature", value=22.0)
humidity = st.number_input("Humidity", min_value=0.0, value=27.0)
light = st.number_input("Light", min_value=0.0, value=400.0)
co2 = st.number_input("CO2", min_value=0.0, value=600.0)

if st.button("Predict Occupancy"):

    new_data = pd.DataFrame([{
        "Temperature": temp,
        "Humidity": humidity,
        "Light": light,
        "CO2": co2
    }])

    prediction = model.predict(new_data)[0]

    if prediction == 1:
        st.success("Room is Occupied")
    else:
        st.success("Room is Not Occupied")
