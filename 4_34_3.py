import requests
from pprint import pprint


def weather(city, days):

    params = {
        'q': city,
        'cnt': days,
        'appid': 'd7fd976e6587ff15ad6479f4c234088d',
        'units': 'metric'
    }

    resp = requests.get('http://api.openweathermap.org/data/2.5/weather/', params=params).json()
    return resp


if __name__ == "__main__":
    while True:
        city = input("City: ")
        if city == "Exit":
            break
        days = input("days: ")
        res = weather(city=city, days=days)
        if int(res['cod']) > 400:
            continue

        pprint(res)

