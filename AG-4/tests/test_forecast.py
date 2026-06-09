from unittest.mock import patch, MagicMock
from src.forecast import get_5_day_forecast


def _make_entry(dt_txt, temp_max, temp_min, humidity, description):
    return {
        "dt_txt": dt_txt,
        "main": {"temp_max": temp_max, "temp_min": temp_min, "humidity": humidity},
        "weather": [{"description": description}],
    }


FAKE_LIST = [
    _make_entry("2024-01-01 09:00:00", 10.0,  5.0, 80, "cloudy"),
    _make_entry("2024-01-01 12:00:00", 12.0,  4.0, 75, "light rain"),
    _make_entry("2024-01-02 09:00:00", 14.0,  6.0, 70, "overcast"),
    _make_entry("2024-01-02 12:00:00", 15.0,  5.5, 65, "clear sky"),
    _make_entry("2024-01-03 09:00:00", 11.0,  3.0, 90, "heavy rain"),
    _make_entry("2024-01-03 12:00:00", 13.0,  2.5, 85, "drizzle"),
    _make_entry("2024-01-04 09:00:00",  9.0,  1.0, 60, "sunny"),
    _make_entry("2024-01-04 12:00:00", 10.0,  0.5, 55, "few clouds"),
    _make_entry("2024-01-05 09:00:00", 16.0,  8.0, 50, "mist"),
    _make_entry("2024-01-05 12:00:00", 17.0,  7.5, 45, "fog"),
]


@patch("src.forecast.requests.get")
def test_returns_five_days(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {"list": FAKE_LIST}
    mock_get.return_value = mock_response

    result = get_5_day_forecast("London", "fake-key")

    assert len(result) == 5

    for item in result:
        assert set(item.keys()) == {"date", "high_temp", "low_temp", "description", "humidity"}
        assert isinstance(item["date"], str)
        assert isinstance(item["high_temp"], float)
        assert isinstance(item["low_temp"], float)
        assert isinstance(item["description"], str)
        assert isinstance(item["humidity"], int)

    day1 = result[0]
    assert day1["date"]        == "2024-01-01"
    assert day1["high_temp"]   == 12.0
    assert day1["low_temp"]    == 4.0
    assert day1["description"] == "light rain"
    assert day1["humidity"]    == 78

    mock_get.assert_called_once_with(
        "https://api.openweathermap.org/data/2.5/forecast",
        params={"q": "London", "appid": "fake-key", "units": "metric"},
    )