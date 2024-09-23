import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the model, scaler, and dictionaries
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
dictionary1 = pickle.load(open("dictionary1.pkl", "rb"))
dictionary2 = pickle.load(open("dictionary2.pkl", "rb"))
dictionary3 = pickle.load(open("dictionary3.pkl", "rb"))

# Streamlit app title
st.title("Cricket Match Outcome Prediction")

# User input for batting team, bowling team, and city
batting_team = st.selectbox("Select Batting Team", list(dictionary1.keys()))
bowling_team = st.selectbox("Select Bowling Team", list(dictionary2.keys()))
selected_city = st.selectbox("Select City", list(dictionary3.keys()))

# User input for runs left, balls left, and wickets left
runs_left = st.number_input("Runs Left", min_value=0, value=220)
balls_left = st.number_input("Balls Left", min_value=0, value=120)
wickets_left = st.number_input("Wickets Left", min_value=0, value=10)
target = st.number_input("Target Runs", min_value=0, value=222)

# Calculate additional metrics
overs = (120 - balls_left) / 6
crr = runs_left / overs if overs > 0 else 0
rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

# Prepare input DataFrame
input_df = pd.DataFrame({
    'batting_team': [batting_team],
    'bowling_team': [bowling_team],
    'city': [selected_city],
    'runs_left': [runs_left],
    'balls_left': [balls_left],
    'wickets_left': [wickets_left],
    'total_runs_x': [target],
    'crr': [crr],
    'rr': [rrr]
})

# Create LabelEncoders and fit them on known categories
batting_encoder = LabelEncoder()
bowling_encoder = LabelEncoder()
city_encoder = LabelEncoder()

# Fit the encoders on the known categories
batting_encoder.fit(list(dictionary1.keys()))
bowling_encoder.fit(list(dictionary2.keys()))
city_encoder.fit(list(dictionary3.keys()))

# Transform categorical variables
input_df['batting_team'] = batting_encoder.transform(input_df['batting_team'])
input_df['bowling_team'] = bowling_encoder.transform(input_df['bowling_team'])
input_df['city'] = city_encoder.transform(input_df['city'])

# Scale numerical features
numerical_cols = input_df.select_dtypes(include=['float64', 'int64']).columns
input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])

# Predict the outcome
if st.button('Predict Probability'):
    result = model.predict(input_df)
    win_prob = result[0][0]
    loss_prob = 1 - win_prob

    st.header(f"{batting_team} - {round(win_prob * 100)}%")
    st.header(f"{bowling_team} - {round(loss_prob * 100)}%")

