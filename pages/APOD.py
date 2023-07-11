import streamlit as st
import requests
import os
from dotenv import load_dotenv


def callApi():
    load_dotenv(".env")


callApi()


api_key = os.getenv('apod_key')


# url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
url = f"https://api.nasa.gov/planetary/apod?api_key={st.secrets('apod_key')}"

response = requests.get(url)
content = response.json()

st.header(":red[Astronomy Picture of the Day]")
st.subheader(f":white[{content['title']}]")

date = content['date']

create_img = "images/image.jpg"
image_url = content['url']
extract_img = requests.get(image_url)

with open(create_img, 'wb') as img:
    img.write(extract_img.content)


st.image("images/image.jpg")
st.write(date)

st.write(f':red[Description on {content["title"]}]')
st.write(f":white[{content['explanation']}]")

