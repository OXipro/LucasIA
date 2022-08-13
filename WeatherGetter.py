import json
import urllib.request
import urllib.parse

OWM_API_KEY = "d2fbaf8626a4be8e58f46f768c0dfc76"
CITY = "Waterloo,BE"
CITY2 = "Waterloo"
OWM_API_BASE_URL = "http://api.openweathermap.org/data/2.5/"


def getWeather():
    content = ""
    weather_gps = json.loads(urllib.request.urlopen(
        OWM_API_BASE_URL + "weather?APPID=" + OWM_API_KEY + "&q=" + urllib.parse.quote_plus(
            CITY.encode("utf8")) + "&mode=json&units=metric").read())

    if 'lon' in weather_gps['coord']:
        gps_lon = str(weather_gps['coord']['lon'])
        gps_lat = str(weather_gps['coord']['lat'])

        weather = json.loads(urllib.request.urlopen(
            OWM_API_BASE_URL + "onecall?APPID=" + OWM_API_KEY + "&lat=" + gps_lat + "&lon=" + gps_lon + "&units=metric&lang=fr&exclude=hourly").read())

        if 'current' in weather:
            current_temp = str(weather['current']['temp'])
            current_temp_feels = str(weather['current']['feels_like'])
            weather_desc = str(weather['current']['weather'][0]['description'])
            day_max_temp = str(weather['daily'][0]['temp']['max'])

            content = "Il fait actuellement " + str(round(int(float(current_temp)))) + " degrées et " + str(
                round(int(float(current_temp_feels)))) + " degrées ressenti à " + CITY2 + "."
            content += "\n"
            content += "Le ciel est " + weather_desc + "."
            content += "\n"
            content += "La température maximale sera de " + str(round(int(float(day_max_temp)))) + " degrées"

    return content
