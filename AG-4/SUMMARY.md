# Project Summary: weather_dashboard_forecast

**Generated:** 2026-06-09 19:08:16
**Complexity:** MEDIUM
**Original Requirement:** Enhance weather dashboard with 5-day forecast

*Description:* Enhance the existing city weather dashboard CLI application to display a 5-day weather forecast in addition to the current weather conditions.

*Acceptance Criteria:*

* When a user runs the app with a city name, it should display current weather as before
* Below current weather, display a 5-day forecast showing:
** Date
** High and low temperature
** Weather description (e.g. clear sky, rain)
** Humidity percentage
* Forecast data should use the same OpenWeatherMap API key
* Output should be clean and readable in the terminal
* All existing tests should still pass
* New tests added for forecast functionality
**Project Summary:** Enhance an existing city weather dashboard CLI to display current conditions plus a 5-day forecast using the OpenWeatherMap API.
**Project Folder:** `output\enhance_weather_dashboard_5day`

---

## Stories Completed: 3/3

### Story 1: Fetch 5-Day Forecast — ✅ DONE

**Requirement:** Create a function `get_5_day_forecast(city, api_key)` in `src/forecast.py` that calls the OpenWeatherMap `/forecast` endpoint and returns a list of 5 daily summaries, each containing date, high temp, low temp, weather description, and humidity.

**Acceptance Criteria:**
- Calling `get_5_day_forecast('London', api_key)` returns a list of exactly 5 items
- Each item contains keys: 'date', 'high_temp', 'low_temp', 'description', 'humidity'
- Values are correctly parsed from the OpenWeatherMap `/forecast` API JSON response
- Unit tests in `tests/test_forecast.py` pass using a mocked API response

**QA Status:** PASS
**Tech Stack:** requests, pytest, python-dotenv

---

### Story 2: Format Forecast Output — ✅ DONE

**Requirement:** Create a function `format_forecast(forecast_list)` in `src/formatter.py` that accepts the forecast list from `get_5_day_forecast` and returns a clean, human-readable multi-line string suitable for terminal display.

**Acceptance Criteria:**
- Calling `format_forecast(forecast_list)` returns a non-empty formatted string
- Output string includes date, high/low temperatures, description, and humidity for each of the 5 days
- Each day is visually separated and readable in a terminal
- Unit tests in `tests/test_formatter.py` pass with sample forecast data

**QA Status:** PASS
**Tech Stack:** pytest

---

### Story 3: Integrate Forecast into CLI — ✅ DONE

**Requirement:** Update the existing CLI entry point so that after displaying current weather, it calls `get_5_day_forecast` and prints the formatted forecast returned by `format_forecast` below the current weather output.

**Acceptance Criteria:**
- Running `py -m src.main London` displays current weather followed by a 5-day forecast section
- The forecast section header (e.g. '5-Day Forecast:') is visible in the output
- All existing current-weather tests still pass without modification
- New integration test in `tests/test_main.py` verifies forecast output appears when CLI runs with a valid city

**QA Status:** PASS
**Tech Stack:** requests, python-dotenv, pytest

---

## How to Run

```bash
cd output\enhance_weather_dashboard_5day
pip install -r requirements.txt
py -m src.main <your_arguments>
```

## Notes for Jira

- Total stories implemented: 3
- All stories are in folder: `output\enhance_weather_dashboard_5day`
- Each story's code is in `src/` subfolder
- Tests are in `tests/` subfolder
