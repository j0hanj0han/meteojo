import os

from meteoblue_wrapper.crawlers import open_weather

# your api_key_here
api_key_openweather  = os.environ["API_KEY"]

if __name__ == "__main__":
    city = 'Paris, FR'
    open_weather.get_weather(city)
    import pdb; pdb.set_trace()