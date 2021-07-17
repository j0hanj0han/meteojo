
import os
from datetime import datetime

from pyowm import OWM

def get_weather_one_call(lat, lon):
    owm = OWM(os.environ["API_KEY"])
    mgr = owm.weather_manager()
    one_call = mgr.one_call(lat=lat, lon=lon, exclude='minutely,hourly', units='metric')
    return one_call

def get_forecast_3d(one_call):
    
    print("today")
    tmp = one_call.current.reference_time()
    date = datetime.fromtimestamp(tmp)
    print(date, one_call.current.temp)
    print('--------')
   
    print('forecast')
    # forecast for 0 day
    tmp = one_call.forecast_daily[0].reference_time()
    date = datetime.fromtimestamp(tmp)
    temp_max = one_call.forecast_daily[0].temp.get("max", None)
    temp_min = one_call.forecast_daily[0].temp.get("min", None)
    print(date, temp_max, temp_min)
    
    return forecast_3d

def convert_timestamp(timestamp):
    date = datetime.fromtimestamp(timestamp)
    return date

if __name__ == "__main__":
    # paris time
    lat = 48.8534
    lon = 2.3488
    one_call = get_weather_one_call(lat, lon)
    forecast = get_forecast_3d(one_call)
    print(forecast)

    
    

    
    