import requests
import pprint
import json
import os 
from datetime import datetime

from PIL import Image


pp = pprint.PrettyPrinter(indent=4)

# your api_key_here
api_key_openweather  = os.environ["API_KEY"]

cities = ['Paris, FR', 'Montpellier, FR', 'Clermont-Ferrand, FR', 'Argences, Fr']

def get_weather(city):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key_openweather}")
    print(response)
    json_data = json.loads(response.text)
    pprint.pprint(json_data)
    return json_data

def get_icon_path(json_data):
    icon_name = json_data["weather"][0]["icon"]
    icon_path = f'./meteojo/icons/{icon_name}.png'
    return icon_path

def get_weather_all():
    # paris
    lat = 48.8534
    lon = 2.3488

    # lat = 43.610769
    # lon = 3.876716
    response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude=hourly,minutely&appid={api_key_openweather}")
    json_data = json.loads(response.text)
    #pprint.pprint(json_data)
    for day in json_data['daily']:
        print(datetime.fromtimestamp(day['dt']), day['temp']['min'], day['temp']['max'])
    return json_data

def get_current_weather_image(icon_path):
    width = 202 
    height = 104

    background  = Image.new( mode = "RGBA", size = (width, height), color = (255, 255, 255) )
    icon = Image.open(icon_path).convert("RGBA")
    foreground =  icon.resize((50,50))

    background.paste(foreground, (0, 0), foreground)
    background.show()

    #background_image.save('background_image.png', 'PNG')

def get_forecast_image(forecasts):
    days  =  forecasts['daily']
    import pdb; pdb.set_trace()
    nb_of_days = len(days)
    icons_paths = []
    # get all icons path
    for d in days: 
        icon_name = d["weather"][0]["icon"]
        path = f'./meteojo/icons/{icon_name}.png'
        icons_paths.append(path)

    images = []
    for path in icons_paths:
        image = Image.open(path)
        images.append(image)
    print(images)
          
    # determine first image size
    width,  height =  images[0].size

    image_result_height = height
    image_result_width = width * len(days)

    image_result  = Image.new( mode = "RGBA", size = (image_result_width, image_result_height), color = (255, 255, 255) )
    paste_position_x = 0
    paste_position_y = 0
    for image in images:
        image = image.convert("RGBA")
        image_result.paste(image, (paste_position_x, paste_position_y), image)
        paste_position_x += width
    image_result.show()

     

    
    




# for city in cities:
    
#     response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key_openweather}")
#     print(response)
#     import pdb; pdb.set_trace()
#     json_data = json.loads(response.text)
#     #print(pp.pprint(json_data))

#     # define the variable we want
#     city_name = json_data['name']
#     weather_text = json_data['weather'][0]['description']
#     temperature_now = json_data['main']['temp']
#     temperature_min = json_data['main']['temp_min']
#     temperature_max = json_data['main']['temp_max']
#     humidity = json_data['main']['humidity']
#     sunrise = datetime.fromtimestamp(json_data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
#     sunset = datetime.fromtimestamp(json_data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')

#     # print the weather forecast
#     print('--------------------------------')
#     print('Météo pour la ville de:', city_name)
#     print("Le temps:", weather_text)
#     print("Temperature actuelle:", temperature_now)
#     print("Temperature minimale:", temperature_min)
#     print("Temperature maximale:", temperature_max)
#     print("Humidité:", humidity, "%")
#     print("Lever du soleil:", sunrise)
#     print("Coucher du soleil:", sunset)
#     print('--------------------------------')
