#!/usr/bin/env python3

import requests
from config import API_KEY, WEATHER_URL

def get_weather(lat, lon):
    url = f"{WEATHER_URL}?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        info = response.json()
        return info
    else:
        return 0