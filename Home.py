import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")


place = st.text_input(label="Place:", key="city")

days = st.slider(label="Forecast Days", min_value=1, max_value=5, key="f_days", help="Select the number of forecasted days")

options = st.selectbox(label="Select data to view", options=["Temperature", "Sky"])

st.subheader(f'{options} for the next {days} days in {place}')


def get_data(days):
    date = ["07-07-2023", "08-07-2023", "09-07-2023"]
    temperature = [23, 25, 19]
    temperature = [days * i for i in temperature]
    return date, temperature


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (c)"})
st.plotly_chart(figure)
