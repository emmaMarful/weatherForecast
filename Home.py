import streamlit as st

st.title("Weather Forecast for the Next Days")


place = st.text_input(label="Place:", key="city")

days = st.slider(label="Forecast Days", min_value=1, max_value=5, key="f_days")

options = st.selectbox(label="Select data to view", options=["Temperature", "Sky"])

st.subheader(f'{options} for the next {days} days in {place}')
