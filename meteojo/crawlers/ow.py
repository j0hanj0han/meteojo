
import os

from datetime import datetime
from pdb import main
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps





def get_weather_one_call(lat, lon):
    owm = OWM(os.environ["API_KEY"])
    mgr = owm.weather_manager()
    one_call = mgr.one_call(lat=lat, lon=lon, exclude='minutely,hourly', units='metric')
    return one_call

if __name__ == "__main__":
    
    lat = 48.8534
    lon = 2.3488
    one_call = get_weather_one_call(lat, lon)
    #print(one_call.current.detailed_status)
    #print(one_call.current.temperature)
    print(one_call.forecast_daily[0].reference_time, one_call.forecast_daily[0].temperature)
    
    
    #current_temp
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
    

    
    
    breakpoint()
    print("-----")