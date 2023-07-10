import requests

api_key = "1c1f23ba08a92cba04deeb875fc9a2a5"


def get_data(place, days=None, kind=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}'

    responds = requests.get(url)
    data = responds.json()
    filteredData = data['list']
    numOfValues = 8*days
    filteredData = filteredData[:numOfValues]
    if kind == "Temperature":
        filteredData = [i["main"][0]['temp'] for i in filteredData]

    if kind == "Sky":
        filteredData = [i['weather'][0]['main'] for i in filteredData]

    return filteredData


if __name__ == "__main__":
    output = get_data("Feyiasi", 2, "Temperature")
    print(output)
