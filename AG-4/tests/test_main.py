import subprocess
import sys
from unittest.mock import patch, MagicMock


def test_forecast_in_output():
    mock_current = {
        "name": "London",
        "sys": {"country": "GB"},
        "main": {"temp": 15.0, "feels_like": 13.0, "humidity": 80},
        "weather": [{"description": "clear sky"}],
        "wind": {"speed": 3.5},
    }
    mock_forecast = {
        "list": [
            {
                "dt_txt": "2024-01-01 12:00:00",
                "main": {"temp": 14.0},
                "weather": [{"description": "cloudy"}],
            },
            {
                "dt_txt": "2024-01-02 12:00:00",
                "main": {"temp": 12.0},
                "weather": [{"description": "rain"}],
            },
        ]
    }

    with patch("src.weather.requests.get") as mock_get:
        response_current = MagicMock()
        response_current.raise_for_status.return_value = None
        response_current.json.return_value = mock_current

        response_forecast = MagicMock()
        response_forecast.raise_for_status.return_value = None
        response_forecast.json.return_value = mock_forecast

        mock_get.side_effect = [response_current, response_forecast]

        import src.main as main_module
        import io
        from contextlib import redirect_stdout
        import sys as _sys

        _sys.argv = ["main", "London"]
        buf = io.StringIO()
        with redirect_stdout(buf):
            main_module.main()

        output = buf.getvalue()
        assert "5-Day Forecast:" in output