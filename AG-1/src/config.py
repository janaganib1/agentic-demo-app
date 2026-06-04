import os
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    """Returns weather API key from environment variable"""
    api_key = os.getenv('WEATHER_API_KEY')
    if not api_key:
        raise ValueError("WEATHER_API_KEY environment variable is required")
    return api_key