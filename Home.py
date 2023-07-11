import streamlit as st
import plotly.express as px
from backend import get_data

st.title(":violet[Weather Forecast for the Next Days]")


place = st.text_input(label="Place:", key="city", placeholder="Kumasi")

days = st.slider(label="Forecast Days", min_value=1, max_value=5, key="f_days",
                 help="Select the number of forecasted days")

options = st.selectbox(label="Select data to view", options=["Temperature", "Sky"])

if days != 1:
    st.subheader(f':red[{options} for the next :blue[{days}] days in :blue[{place}]]')
else:
    st.subheader(f':red[{options} for the next day in] :blue[{place}]')

try:
    if place:
        dataExtract = get_data(place, days)

        if options == "Temperature":
            date = [i['dt_txt'] for i in dataExtract]
            filteredData = [i["main"]['temp'] - 273.15 for i in dataExtract]

            figure = px.line(x=date, y=filteredData, labels={"x": "Date", "y": "Temperature (c)"})
            st.plotly_chart(figure)
        else:
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                      "Snow": "images/rain.png"}

            date = [i['dt_txt'] for i in dataExtract]
            skyState = [i['weather'][0]['main'] for i in dataExtract]
            images_path = [images[condition]for condition in skyState]

            st.image(images_path, width=115, caption=date)
except KeyError:
    st.warning(":orange[ENTER A VALID PLACE]", icon="⚠️")
