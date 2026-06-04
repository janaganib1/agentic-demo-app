import argparse
from .weather import get_hourly_forecast

def parse_arguments() -> str:
    """Parses zip code from command line arguments"""
    parser = argparse.ArgumentParser(description='Get hourly weather forecast')
    parser.add_argument('zipcode', help='US zip code (e.g., 12345)')
    args = parser.parse_args()
    return args.zipcode

def main():
    """Entry point that coordinates argument parsing and weather display"""
    try:
        zipcode = parse_arguments()
        forecast = get_hourly_forecast(zipcode)
        print(f"\nHourly Weather Forecast for {zipcode}:\n")
        print(forecast)
    except Exception as e:
        print(f"Error: {e}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())