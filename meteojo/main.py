import os

from meteojo.crawlers import open_weather

# your api_key_here
api_key_openweather  = os.environ["API_KEY"]

if __name__ == "__main__":
    city = 'Paris, FR'
    weather_data = open_weather.get_weather(city)
    open_weather.show_weather_icon(weather_data)
