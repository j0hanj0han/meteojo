import requests
import pprint
import json 
from datetime import datetime

pp = pprint.PrettyPrinter(indent=4)

# your api_key_here
api_key_openweather  = os.environ["API_KEY"]

cities = ['Paris, FR', 'Montpellier, FR', 'Clermont-Ferrand, FR', 'Argences, Fr']
for city in cities:

    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&mode=json&APPID={api_key_openweather}")
    json_data = json.loads(response.text)
    #print(pp.pprint(json_data))

    # define the variable we want
    city_name = json_data['name']
    weather_text = json_data['weather'][0]['description']
    temperature_now = json_data['main']['temp']
    temperature_min = json_data['main']['temp_min']
    temperature_max = json_data['main']['temp_max']
    humidity = json_data['main']['humidity']
    sunrise = datetime.fromtimestamp(json_data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
    sunset = datetime.fromtimestamp(json_data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')

    # print the weather forecast
    print('--------------------------------')
    print('Météo pour la ville de:', city_name)
    print("Le temps:", weather_text)
    print("Temperature actuelle:", temperature_now)
    print("Temperature minimale:", temperature_min)
    print("Temperature maximale:", temperature_max)
    print("Humidité:", humidity, "%")
    print("Lever du soleil:", sunrise)
    print("Coucher du soleil:", sunset)
    print('--------------------------------')