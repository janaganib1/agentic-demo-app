# Project Summary: weather_dashboard_forecast

**Generated:** 2026-06-09 18:10:05
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
**Project Summary:** Enhance an existing city weather CLI dashboard to display a 5-day forecast alongside current conditions using the OpenWeatherMap API.
**Project Folder:** `output\city_weather_dashboard`

---

## Stories Completed: 3/3

### Story 1: Fetch Forecast Data — ✅ DONE

**Requirement:** Create a function `get_5_day_forecast(city, api_key)` that calls the OpenWeatherMap forecast endpoint and returns a list of 5 daily entries each containing date, high temp, low temp, weather description, and humidity.

**Acceptance Criteria:**
- Calling `get_5_day_forecast('London', api_key)` returns a list of exactly 5 items
- Each item contains keys: 'date', 'high_temp', 'low_temp', 'description', 'humidity'
- Values are correctly parsed from the OpenWeatherMap /forecast API JSON response
- Unit tests mock the API response and assert correct parsing of all 5 forecast entries

**QA Status:** PASS
**Tech Stack:** See requirements.txt

---

### Story 2: Format Forecast Output — ✅ DONE

**Requirement:** Create a function `format_forecast(forecast_list)` that accepts the list returned by `get_5_day_forecast` and returns a formatted multi-line string showing each day's date, high/low temps, description, and humidity suitable for terminal display.

**Acceptance Criteria:**
- Calling `format_forecast(forecast_list)` returns a non-empty string
- The returned string contains each of the 5 dates
- Each day's block includes high temp, low temp, weather description, and humidity percentage
- Unit tests assert the formatted output string contains expected values from a sample forecast list

**QA Status:** PASS
**Tech Stack:** See requirements.txt

---

### Story 3: Integrate Forecast CLI — ✅ DONE

**Requirement:** Update the existing CLI entry point so that after displaying current weather it calls `get_5_day_forecast` and prints the result of `format_forecast` below the current conditions.

**Acceptance Criteria:**
- Running `py -m src.main London` displays current weather followed by a 5-day forecast section
- The forecast section is visually separated from current weather with a header or divider line
- All previously passing tests still pass without modification
- A new integration test verifies that running the CLI with a city name prints both current weather and 5 forecast days

**QA Status:** PASS
**Tech Stack:** See requirements.txt

---

## How to Run

```bash
cd output\city_weather_dashboard
pip install -r requirements.txt
py -m src.main <your_arguments>
```

## Notes for Jira

- Total stories implemented: 3
- All stories are in folder: `output\city_weather_dashboard`
- Each story's code is in `src/` subfolder
- Tests are in `tests/` subfolder
