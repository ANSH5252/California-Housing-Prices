import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
feature_columns = pickle.load(open("features.pkl", "rb")) 

st.title(":blue[California House Price Prediction] 🏠")

median_income = st.number_input("Median Income (in $1000s)", min_value=0.0, max_value=20.0, value=5.0)
housing_median_age = st.number_input("Housing Median Age", min_value=1, max_value=100, value=30)
total_rooms = st.number_input("Total Rooms", min_value=1, max_value=10000, value=2000)
total_bedrooms = st.number_input("Total Bedrooms", min_value=1, max_value=5000, value=500)
population = st.number_input("Population", min_value=1, max_value=20000, value=1500)
households = st.number_input("Households", min_value=1, max_value=5000, value=400)
latitude = st.number_input("Latitude", min_value=32.0, max_value=42.0, value=34.0)
longitude = st.number_input("Longitude", min_value=-125.0, max_value=-114.0, value=-118.0)

ocean_proximity = st.selectbox("Ocean Proximity", ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'])

bedrooms_ratio = total_bedrooms / total_rooms
household_rooms = total_rooms / households

log_total_rooms = np.log(total_rooms + 1)
log_total_bedrooms = np.log(total_bedrooms + 1)
log_population = np.log(population + 1)
log_households = np.log(households + 1)

input_dict = {
    'median_income': median_income,
    'housing_median_age': housing_median_age,
    'total_rooms': log_total_rooms,
    'total_bedrooms': log_total_bedrooms,
    'population': log_population,
    'households': log_households,
    'latitude': latitude,
    'longitude': longitude,
    'bedrooms_ratio': bedrooms_ratio,
    'household_rooms': household_rooms
}

input_df = pd.DataFrame([input_dict])

ocean_df = pd.get_dummies(pd.Series([ocean_proximity]), prefix='', prefix_sep='')

for category in ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN']:
    if category not in ocean_df.columns:
        ocean_df[category] = 0

ocean_df = ocean_df[['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN']]

input_df = pd.concat([input_df, ocean_df], axis=1)

input_df = input_df.reindex(columns=feature_columns, fill_value=0)

scaled_input = scaler.transform(input_df)

if st.button("Predict House Price"):
    prediction = model.predict(scaled_input)[0]
    st.success(f"🏡 Estimated House Price: ${int(prediction):,}")