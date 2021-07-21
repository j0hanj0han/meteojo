
import os
from datetime import datetime
from typing import Sized

from pyowm import OWM
from pyowm.weatherapi25.one_call import OneCall

from PIL import Image, ImageFont, ImageDraw

from meteojo.utils import image


def get_weather_one_call(lat, lon):
    owm = OWM(os.environ["API_KEY"])
    mgr = owm.weather_manager()
    one_call = mgr.one_call(lat=lat, lon=lon, exclude='minutely,hourly', units='metric')
    return one_call

def get_forecast_3d(one_call):
    forecast_3d = []
    # today
    tmp = one_call.current.reference_time()
    date = datetime.fromtimestamp(tmp)
    print(date, one_call.current.temp)
    print('--------')

    
    # get forecast for 3 days
    for i in range(0,4):
        tmp = one_call.forecast_daily[i].reference_time()
        date = convert_timestamp(tmp)
        temp_max = one_call.forecast_daily[i].temp.get("max", None)
        temp_min = one_call.forecast_daily[i].temp.get("min", None)
        icon_name = one_call.forecast_daily[i].weather_icon_name
        icon_path = image.get_icon(icon_name)

        forecast = [date, temp_max, temp_min, icon_path]
        forecast_3d.append(forecast)
    
    return forecast_3d

def get_image(forecasts):
    nb_of_days = len(forecasts)
    images = []
    # get all icons path
    for day in forecasts: 
        path = day[3]
        image = Image.open(path)

        image = image.convert("RGBA")
        draw = ImageDraw.Draw(image, 'RGBA')
        font = ImageFont.load_default()
        draw.text(xy=(0,0),text=f"max:{day[1]}/min:{day[2]}", fill=(0, 0,0, 255))
        draw.text(xy=(25,117),text=f"{day[0].split(',')[0]}", fill=(0, 0,0, 255))
        images.append(image)


    # determine first image size
    width,  height =  images[0].size

    image_result_height = height
    image_result_width = width * len(forecasts)

    image_result  = Image.new( mode = "RGBA", size = (image_result_width, image_result_height), color = (255, 255, 255) )
    paste_position_x = 0
    paste_position_y = 0
    for image in images:
        #image = image.convert("RGBA")
        image_result.paste(image, (paste_position_x, paste_position_y), image)
        paste_position_x += width
    image_result.show()



def convert_timestamp(timestamp):
    date = datetime.fromtimestamp(timestamp)
    date = date.strftime("%m/%d/%Y, %H:%M:%S")
    return date

if __name__ == "__main__":
    # paris 
    lat = 48.8534
    lon = 2.3488
    # mtp
    lat = 43.6
    lon = 3.8833


    one_call = get_weather_one_call(lat, lon)
    forecast = get_forecast_3d(one_call)
    for i in forecast:
        print(i)


    get_image(forecast)

    
    

    
    