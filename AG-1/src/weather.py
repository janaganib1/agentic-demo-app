import requests
from .config import get_api_key

def fetch_weather_data(zipcode: str) -> dict:
    """Makes API call and returns JSON response"""
    api_key = get_api_key()
    url = f"http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'zip': f"{zipcode},US",
        'appid': api_key,
        'units': 'imperial'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch weather data: {e}")

def format_hourly_forecast(weather_data: dict) -> str:
    """Formats hourly data for console display"""
    if 'list' not in weather_data:
        raise ValueError("Invalid weather data format")
    
    output = f"{'Time':<15} {'Temp':<8} {'Conditions'}\n"
    output += "-" * 50 + "\n"
    
    # Display first 12 hours
    for item in weather_data['list'][:12]:
        time = item['dt_txt']
        temp = f"{int(item['main']['temp'])}°F"
        conditions = item['weather'][0]['description'].title()
        output += f"{time:<15} {temp:<8} {conditions}\n"
    
    return output

def get_hourly_forecast(zipcode: str) -> str:
    """Orchestrates API call and formatting"""
    weather_data = fetch_weather_data(zipcode)
    return format_hourly_forecast(weather_data)