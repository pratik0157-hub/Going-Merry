#!/usr/bin/env python3

from cli import parse_arguments
from geocode import get_coordinates
from weather import get_weather
from display import choose_location, weather_info

city_name = parse_arguments()

locations = get_coordinates(city_name)

if locations:
    lat, lon = choose_location(locations)

    weather = get_weather(lat, lon)

    if weather:
        weather_info(weather)
    else:
        print("Invalid input. Please try again.")
else:
    print("Invalid input. Please try again.")