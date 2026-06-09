# Project Summary: weather_dashboard_forecast

**Generated:** 2026-06-09 19:00:29
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
**Project Summary:** Enhance the existing city weather dashboard CLI to display a 5-day forecast alongside current weather using the OpenWeatherMap API.
**Project Folder:** `output\weather_dashboard_forecast`

---

## Stories Completed: 3/3

### Story 1: Fetch Forecast Data — ✅ DONE

**Requirement:** Create a function `get_5day_forecast(city, api_key)` that calls the OpenWeatherMap forecast endpoint and returns a list of 5 daily summaries each containing date, high temp, low temp, weather description, and humidity.

**Acceptance Criteria:**
- Calling `get_5day_forecast('London', api_key)` returns a list of exactly 5 items
- Each item contains keys: 'date', 'high_temp', 'low_temp', 'description', 'humidity'
- Values are correctly parsed from the OpenWeatherMap `/forecast` API response
- Unit tests mock the API response and assert correct parsing for all 5 days

**QA Status:** PASS
**Tech Stack:** See requirements.txt

---

### Story 2: Format Forecast Output — ✅ DONE

**Requirement:** Create a function `format_forecast(forecast_list)` that accepts the list returned by `get_5day_forecast` and returns a clean, human-readable multi-line string suitable for terminal display.

**Acceptance Criteria:**
- Calling `format_forecast(forecast_list)` returns a non-empty string
- Output string contains each day's date, high/low temperatures, description, and humidity percentage
- Each day is visually separated so the output is easy to read in a terminal
- Unit tests assert the formatted string contains expected values for a mocked forecast list

**QA Status:** PASS
**Tech Stack:** See requirements.txt

---

### Story 3: Integrate Forecast CLI — ✅ DONE

**Requirement:** Update the existing CLI entry point so that after displaying current weather it calls `get_5day_forecast` and prints the output of `format_forecast` below the current conditions.

**Acceptance Criteria:**
- Running `py -m src.main London` displays current weather followed by the 5-day forecast
- The forecast section is clearly labeled (e.g. '5-Day Forecast:') in the terminal output
- All pre-existing tests still pass without modification
- New integration test mocks both API calls and asserts both current weather and forecast sections appear in the output

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
