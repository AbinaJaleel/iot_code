
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay

# Dashboard
st.title(Air Quality Index Dashboard)
st.write(AQI Prediction using Random Forest)
st.divider()

# Read dataset
data = pd.read_csv(city_day.csv)
df = pd.DataFrame(data)

st.subheader(Dataset)
st.write(Total Rows, len(df))
st.dataframe(df.head())

# Features and target
features = [PM2.5, PM10, NO2, CO, SO2, O3]
target = AQI_Bucket

df = df[features + [target]]
df = df.dropna(subset=features + [target])

# Statistical analysis
st.subheader(Statistical Analysis)
st.dataframe(df[features].describe())

# Split data
x = df[features]
y = df[target]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(x_train, y_train)

# Prediction and evaluation
pred = model.predict(x_test)
accuracy = accuracy_score(y_test, pred)

st.subheader(Model Accuracy)
st.metric(Accuracy, f{accuracy100.2f}%)

# Confusion Matrix
st.subheader(Confusion Matrix)
fig, ax = plt.subplots()
ConfusionMatrixDisplay.from_predictions(y_test, pred, ax=ax)
st.pyplot(fig)

# User input
st.subheader(Enter Pollutant Values)

pm25 = st.number_input(PM2.5, min_value=0.0, value=50.0)
pm10 = st.number_input(PM10, min_value=0.0, value=80.0)
no2 = st.number_input(NO2, min_value=0.0, value=20.0)
co = st.number_input(CO, min_value=0.0, value=1.0)
so2 = st.number_input(SO2, min_value=0.0, value=10.0)
o3 = st.number_input(O3, min_value=0.0, value=30.0)

if st.button(Predict AQI)

    new_data = pd.DataFrame([{
        PM2.5 pm25,
        PM10 pm10,
        NO2 no2,
        CO co,
        SO2 so2,
        O3 o3
    }])

    prediction = model.predict(new_data)[0]

    st.success(Predicted AQI Bucket  + prediction)
