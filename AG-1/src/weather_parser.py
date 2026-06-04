import json
from datetime import datetime
from .config import TIME_FORMAT

def parse_hourly_forecast(api_response: dict) -> str:
    """Main function that extracts hourly data and returns formatted string"""
    if not api_response or 'hourly' not in api_response:
        return "No hourly forecast data available"
    
    hourly_data = api_response['hourly']
    if not hourly_data:
        return "No hourly forecast data available"
    
    formatted_hours = []
    for hour_data in hourly_data:
        formatted_hour = format_hour_data(hour_data)
        if formatted_hour:
            formatted_hours.append(formatted_hour)
    
    return '\n'.join(formatted_hours) if formatted_hours else "No valid forecast data"

def format_hour_data(hour_data: dict) -> str:
    """Formats single hour's temperature and condition into readable text"""
    try:
        time_str = extract_time_string(hour_data.get('dt', ''))
        temp = hour_data.get('temp', 'N/A')
        weather_list = hour_data.get('weather', [])
        condition = weather_list[0].get('description', 'Unknown') if weather_list else 'Unknown'
        
        return f"{time_str} - {temp}°F, {condition.title()}"
    except (KeyError, IndexError, TypeError):
        return ""

def extract_time_string(timestamp) -> str:
    """Converts API timestamp to readable hour format"""
    try:
        if isinstance(timestamp, (int, float)):
            dt = datetime.fromtimestamp(timestamp)
        elif isinstance(timestamp, str):
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        else:
            return "Unknown Time"
        
        return dt.strftime(TIME_FORMAT)
    except (ValueError, OSError):
        return "Unknown Time"