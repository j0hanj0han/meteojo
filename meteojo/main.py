import os

from meteojo.crawlers import open_weather

# your api_key_here
api_key_openweather  = os.environ["API_KEY"]

if __name__ == "__main__":
    city = 'Paris, FR'
    #weather_data = open_weather.get_weather(city)
    #icon_path = open_weather.get_icon_path(weather_data)
    
    #open_weather.get_current_weather_image(icon_path)

    forecasts = open_weather.get_weather_all()
    open_weather.get_forecast_image(forecasts)


