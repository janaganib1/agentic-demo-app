# Project Summary: weather_dashboard_cli

**Generated:** 2026-06-08 21:57:30
**Complexity:** MEDIUM
**Original Requirement:** Develop a weather dashboard for a city name

Create a CLI application that accepts a city name
as input and displays the current weather conditions
including temperature, humidity, wind speed, and a
brief weather description.

Use the OpenWeatherMap API key from {{.ENV file WEATHER_API_KEY}}


Example usage: py -m src.main "Dallas"
**Project Summary:** A CLI application that accepts a city name and displays current weather conditions using the OpenWeatherMap API.
**Project Folder:** `output\weather_dashboard_cli`

---

## Stories Completed: 3/3

### Story 1: Fetch Weather API Data — ✅ DONE

**Requirement:** Create a core module in src/weather.py that reads WEATHER_API_KEY from a .env file and fetches current weather data for a given city name from the OpenWeatherMap API, returning temperature, humidity, wind speed, and weather description as a dictionary.

**Acceptance Criteria:**
- Calling get_weather('Dallas') returns a dictionary with keys: city, temperature, humidity, wind_speed, and description
- WEATHER_API_KEY is loaded from .env file using python-dotenv
- Function returns correct values matching the OpenWeatherMap API response for a valid city name

**QA Status:** PASS
**Tech Stack:** requests, python-dotenv, pytest

---

### Story 2: Format Weather Output — ✅ DONE

**Requirement:** Create a display module in src/display.py with a function that accepts the weather dictionary from the core module and formats it into a readable multi-line CLI output showing city, temperature, humidity, wind speed, and description.

**Acceptance Criteria:**
- Calling format_weather(weather_dict) returns a formatted string containing city name, temperature, humidity, wind speed, and description
- Output is human-readable with labeled fields and appropriate units (e.g., °C or °F, %, km/h)

**QA Status:** PASS
**Tech Stack:** requests, python-dotenv, pytest

---

### Story 3: Build CLI Entry Point — ✅ DONE

**Requirement:** Create src/main.py as the CLI entry point that accepts a city name as a command-line argument, calls the weather fetch function, passes the result to the display formatter, and prints the formatted output to the terminal.

**Acceptance Criteria:**
- Running py -m src.main 'Dallas' prints formatted weather output for Dallas including temperature, humidity, wind speed, and description
- Running py -m src.main without arguments prints a usage error message
- Application exits without error for a valid city name

**QA Status:** PASS
**Tech Stack:** requests, python-dotenv, pytest

---

## How to Run

```bash
cd output\weather_dashboard_cli
pip install -r requirements.txt
py -m src.main <your_arguments>
```

## Notes for Jira

- Total stories implemented: 3
- All stories are in folder: `output\weather_dashboard_cli`
- Each story's code is in `src/` subfolder
- Tests are in `tests/` subfolder
