# Project Summary: weather_dashboard_forecast

**Generated:** 2026-06-09 18:52:21
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
**Project Summary:** Enhance an existing city weather dashboard CLI to display a 5-day forecast with date, high/low temps, description, and humidity alongside current conditions using the OpenWeatherMap API.
**Project Folder:** `output\weather_dashboard_forecast`

---

## Stories Completed: 3/3

### Story 1: Fetch 5-Day Forecast Data — ✅ DONE

**Requirement:** Create a function `get_5day_forecast(city, api_key)` in `src/forecast.py` that calls the OpenWeatherMap `/forecast` endpoint and returns a list of 5 daily summaries each containing date, high temp, low temp, weather description, and humidity.

**Acceptance Criteria:**
- Calling `get_5day_forecast('London', api_key)` returns a list of exactly 5 items
- Each item contains keys: 'date', 'high', 'low', 'description', 'humidity'
- Unit test with mocked HTTP response passes and validates returned data structure
- Function raises a clear exception when the city is not found (non-200 response)

**QA Status:** PASS
**Tech Stack:** See requirements.txt

---

### Story 2: Format Forecast Output — ✅ DONE

**Requirement:** Create a function `format_forecast(forecast_list)` in `src/forecast.py` that accepts the list returned by `get_5day_forecast` and returns a formatted multi-line string showing date, high/low temperature, weather description, and humidity for each day.

**Acceptance Criteria:**
- Calling `format_forecast(sample_list)` returns a non-empty string containing all 5 dates
- Output string includes high temp, low temp, description, and humidity for each day
- Unit test with sample forecast data asserts all expected fields appear in the returned string
- Running `py -m pytest tests/test_forecast.py` passes all new and existing tests

**QA Status:** PASS
**Tech Stack:** See requirements.txt

---

### Story 3: Integrate Forecast Into CLI — ✅ DONE

**Requirement:** Update the existing CLI entry point in `src/main.py` to call `get_5day_forecast` and `format_forecast` after displaying current weather, printing the 5-day forecast section below with a clear header separator.

**Acceptance Criteria:**
- Running `py -m src.main London` displays current weather followed by a '5-Day Forecast' section
- Forecast section shows 5 days of date, high/low temp, description, and humidity
- All previously passing tests still pass after the update
- Running `py -m src.main InvalidCityXYZ` prints an error message and exits without a stack trace

**QA Status:** PASS
**Tech Stack:** See requirements.txt

---

## How to Run

```bash
cd output\weather_dashboard_forecast
pip install -r requirements.txt
py -m src.main <your_arguments>
```

## Notes for Jira

- Total stories implemented: 3
- All stories are in folder: `output\weather_dashboard_forecast`
- Each story's code is in `src/` subfolder
- Tests are in `tests/` subfolder
