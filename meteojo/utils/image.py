



def get_icon(icon_name):
    icon_name = json_data["weather"][0]["icon"]
    icon = f'./meteojo/icons/{icon_name}.png'
    return icon


def get_weather_image():
    pass