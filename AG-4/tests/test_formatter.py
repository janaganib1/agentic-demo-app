# tests/test_formatter.py

from src.formatter import format_forecast

SAMPLE_FORECAST = [
    {"date": "2024-06-01", "temp_high": 28, "temp_low": 18, "description": "Sunny",        "humidity": 40},
    {"date": "2024-06-02", "temp_high": 25, "temp_low": 17, "description": "Partly cloudy", "humidity": 55},
    {"date": "2024-06-03", "temp_high": 22, "temp_low": 15, "description": "Rainy",         "humidity": 80},
    {"date": "2024-06-04", "temp_high": 20, "temp_low": 13, "description": "Thunderstorm",  "humidity": 90},
    {"date": "2024-06-05", "temp_high": 24, "temp_low": 16, "description": "Cloudy",        "humidity": 65},
]


def test_format_forecast_returns_nonempty_string():
    result = format_forecast(SAMPLE_FORECAST)
    assert isinstance(result, str)
    assert len(result) > 0


def test_format_forecast_contains_all_dates():
    result = format_forecast(SAMPLE_FORECAST)
    for day in SAMPLE_FORECAST:
        assert day["date"] in result


def test_format_forecast_contains_all_temperatures():
    result = format_forecast(SAMPLE_FORECAST)
    for day in SAMPLE_FORECAST:
        assert str(day["temp_high"]) in result
        assert str(day["temp_low"]) in result


def test_format_forecast_contains_all_descriptions():
    result = format_forecast(SAMPLE_FORECAST)
    for day in SAMPLE_FORECAST:
        assert day["description"] in result


def test_format_forecast_contains_all_humidity_values():
    result = format_forecast(SAMPLE_FORECAST)
    for day in SAMPLE_FORECAST:
        assert str(day["humidity"]) in result


def test_format_forecast_contains_separator():
    result = format_forecast(SAMPLE_FORECAST)
    assert "─" * 30 in result