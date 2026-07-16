#!/usr/bin/env python3

import requests
from config import API_KEY, GEOCODE_URL

def get_coordinates(city):
    url = f"{GEOCODE_URL}?q={city}&limit=5&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        coordinates = response.json()
        return coordinates
    else:
        return 0


    