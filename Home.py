import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the Next Days")


place = st.text_input(label="Place:", key="city")

days = st.slider(label="Forecast Days", min_value=1, max_value=5, key="f_days", help="Select the number of forecasted days")

options = st.selectbox(label="Select data to view", options=["Temperature", "Sky"])

if days != 1:
    st.subheader(f'{options} for the next {days} days in {place}')
else:
    st.subheader(f'{options} for the next day in {place}')

t = get_data(place, days, options)


if options == "Temperature":
    figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (c)"})
    st.plotly_chart(figure)
else:
    st.image()
