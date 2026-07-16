#!/usr/bin/env python3


def choose_location(geo_pos):
    if len(geo_pos) > 1:
            print("Multiple locations formed:")
            for i in range(len(geo_pos)):
                    city = geo_pos[i]
                    print(f"{i+1}. {city['name']}, {city['state']}, {city['country']}")
            num = int(input("Enter the correct choice: "))
            final_city = geo_pos[num-1]
    else:
            final_city = geo_pos[0]     

    lat = final_city['lat']
    lon = final_city['lon']
    return lat, lon

def weather_info(data):
       print("City:", data["name"])
       print("Temperature:", data["main"]["temp"])
       print("Humidity:", data["main"]["humidity"])
       print("Pressure:", data["main"]["pressure"])
       print("Weather:", data["weather"][0]["description"])
       print("Wind Speed:", data["wind"]["speed"])
       