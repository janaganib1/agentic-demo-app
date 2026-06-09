import argparse
from src.weather import get_current_weather, format_current_weather, get_5_day_forecast, format_forecast


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch weather for a city")
    parser.add_argument("city", help="City name")
    args = parser.parse_args()

    current = get_current_weather(args.city)
    print(format_current_weather(current))

    forecast_data = get_5_day_forecast(args.city)
    print(format_forecast(forecast_data))


if __name__ == "__main__":
    main()