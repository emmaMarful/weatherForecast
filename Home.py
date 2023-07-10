import streamlit as st
import plotly.express as px
import backend as bc

st.title("Weather Forecast for the Next Days")


place = st.text_input(label="Place:", key="city")

days = st.slider(label="Forecast Days", min_value=1, max_value=5, key="f_days", help="Select the number of forecasted days")

options = st.selectbox(label="Select data to view", options=["Temperature", "Sky"])

st.subheader(f'{options} for the next {days} days in {place}')

d, t = bc.get_data(place, days, options)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (c)"})
st.plotly_chart(figure)
