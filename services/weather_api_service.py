from geopy.geocoders import Nominatim
from geopy.location import Location
import httpx
import requests

geolocator = Nominatim(user_agent="myapplication")
location: Location = geolocator.geocode("Chicago Illinois")
print(type(location))
api_key = None


def get_geo_codes(search_string):
    geolocator = Nominatim(user_agent="myapplication")
    location = geolocator.geocode(search_string)
    # prequests
    return location


def get_weather_data(city: str, state: str, country: str):
    search_str = f"{city} {state} {country}"
    location: Location = get_geo_codes(search_str)
    # return {"data": f"{location.address}"}
    res = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={api_key}"
    )
    print(res.status_code)

    # return {"data": f"{location.latitude} {location.longitude}"}
    return res.json()["main"]


async def get_weather_data_async(city: str, state: str, country: str):
    search_str = f"{city} {state} {country}"
    location: Location = get_geo_codes(search_str)
    # return {"data": f"{location.address}"}
    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={api_key}"
        )

    print(res.status_code)

    # return {"data": f"{location.latitude} {location.longitude}"}
    return res.json()["main"]
