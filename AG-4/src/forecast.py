import requests
from collections import defaultdict

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_5_day_forecast(city: str, api_key: str) -> list:
    response = requests.get(BASE_URL, params={
        "q": city,
        "appid": api_key,
        "units": "metric",
    })
    response.raise_for_status()
    entries = response.json()["list"]

    grouped = defaultdict(list)
    for entry in entries:
        date = entry["dt_txt"][:10]
        grouped[date].append(entry)

    first_five_dates = list(grouped.keys())[:5]

    result = []
    for date in first_five_dates:
        day_entries = grouped[date]

        high_temp = max(e["main"]["temp_max"] for e in day_entries)
        low_temp  = min(e["main"]["temp_min"] for e in day_entries)
        humidity  = round(sum(e["main"]["humidity"] for e in day_entries) / len(day_entries))

        noon_entries = [e for e in day_entries if "12:00:00" in e["dt_txt"]]
        desc_entry = noon_entries[0] if noon_entries else day_entries[0]
        description = desc_entry["weather"][0]["description"]

        result.append({
            "date":        date,
            "high_temp":   high_temp,
            "low_temp":    low_temp,
            "description": description,
            "humidity":    humidity,
        })

    return result