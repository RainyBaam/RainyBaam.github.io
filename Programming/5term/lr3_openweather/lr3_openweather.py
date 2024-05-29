import requests

api_key = "5ceca24aef4fdfd07f003be896f85257"
url = "https://api.openweathermap.org/data/2.5/weather?q=" \
      "Saint Petersburg&appid=5ceca24aef4fdfd07f003be896f85257"


def get_weather_data(place, key=api_key):
    res = requests.get(
        url,
        params={
            "q": place,
            "appid": key,
            "units": "metric"
        }
    )

    return res.text


if __name__ == "__main__":
    print(get_weather_data("Saint Petersburg"))
