import requests
from .config import WEATHER_API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5"


def get_current_weather(city: str) -> dict:
    url = f"{BASE_URL}/weather"
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric",
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def format_current_weather(data: dict) -> str:
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"].capitalize()
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    return (
        f"Current Weather for {city}, {country}:\n"
        f"  {description}\n"
        f"  Temperature: {temp}°C (Feels like {feels_like}°C)\n"
        f"  Humidity: {humidity}%\n"
        f"  Wind Speed: {wind_speed} m/s"
    )


def get_5_day_forecast(city: str) -> dict:
    url = f"{BASE_URL}/forecast"
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric",
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def format_forecast(forecast_data: dict) -> str:
    lines = ["5-Day Forecast:"]
    seen_dates = []
    for item in forecast_data["list"]:
        date = item["dt_txt"].split(" ")[0]
        if date not in seen_dates:
            seen_dates.append(date)
            temp = item["main"]["temp"]
            description = item["weather"][0]["description"].capitalize()
            lines.append(f"  {date}: {description}, {temp}°C")
        if len(seen_dates) == 5:
            break
    return "\n".join(lines)