import requests
import os
from dotenv import load_dotenv


def callApi():
   load_dotenv(".env")



callApi()

api_key = os.getenv("weather_key")


def get_data(place, days=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}'

    responds = requests.get(url)
    data = responds.json()
    filteredData = data['list']
    numOfValues = 8*days
    filteredData = filteredData[:numOfValues]

    return filteredData


if __name__ == "__main__":
    output = get_data("Feyiasi", 1)
    print(output)