# Project Summary: weather_dashboard_forecast

**Generated:** 2026-06-09 18:28:33
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
**Project Summary:** Enhance an existing city weather dashboard CLI to display a 5-day forecast alongside current conditions using the OpenWeatherMap API.
**Project Folder:** `output\city_weather_dashboard`

---

## Stories Completed: 3/3

### Story 1: Fetch Forecast Data — ✅ DONE

**Requirement:** Create a function `get_5day_forecast(city, api_key)` that calls the OpenWeatherMap 5-day forecast endpoint and returns a list of 5 daily summaries each containing date, high temp, low temp, weather description, and humidity.

**Acceptance Criteria:**
- Calling `get_5day_forecast('London', api_key)` returns a list of exactly 5 items
- Each item contains keys: 'date', 'high_temp', 'low_temp', 'description', 'humidity'
- Dates returned are 5 distinct future calendar days
- Unit tests cover the parsing logic using a mocked API response

**QA Status:** PASS
**Tech Stack:** See requirements.txt

---

### Story 2: Format Forecast Output — ✅ DONE

**Requirement:** Create a function `format_forecast(forecast_list)` that accepts the list returned by `get_5day_forecast` and returns a clean, human-readable multi-line string suitable for terminal display.

**Acceptance Criteria:**
- Calling `format_forecast(sample_forecast)` returns a string containing each day's date, high/low temps, description, and humidity
- Output is visually separated per day with consistent alignment
- Unit tests confirm expected string output for a known sample input

**QA Status:** PASS
**Tech Stack:** See requirements.txt

---

### Story 3: Integrate Forecast into CLI — ✅ DONE

**Requirement:** Update the existing CLI entry point so that after displaying current weather it calls `get_5day_forecast` and prints the formatted forecast returned by `format_forecast`, using the same city argument and API key.

**Acceptance Criteria:**
- Running `py -m src.main London` displays current weather followed by a clearly labelled 5-day forecast section
- All previously passing tests continue to pass
- New integration test confirms forecast section appears in CLI output when run with a valid city name

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
