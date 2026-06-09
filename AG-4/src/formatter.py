# src/formatter.py

SEPARATOR = "─" * 30


def format_forecast(forecast_list: list) -> str:
    """
    Convert a list of 5-day forecast dicts into a clean,
    human-readable multi-line string for terminal display.

    Each dict must contain: date, temp_high, temp_low,
    description, humidity.

    Returns a single multi-line string (does not print).
    """
    blocks = []

    for day in forecast_list:
        date        = day["date"]
        temp_high   = day["temp_high"]
        temp_low    = day["temp_low"]
        description = day["description"]
        humidity    = day["humidity"]

        block = (
            f"{date}\n"
            f"  High      : {temp_high}°\n"
            f"  Low       : {temp_low}°\n"
            f"  Condition : {description}\n"
            f"  Humidity  : {humidity}%"
        )
        blocks.append(block)

    return f"\n{SEPARATOR}\n".join(blocks)