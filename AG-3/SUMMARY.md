# Project Summary: city_weather_dashboard

**Generated:** 2026-06-08 21:24:39
**Complexity:** MEDIUM
**Original Requirement:** Develop a weather dashboard for a city name

Create a CLI application that accepts a city name
as input and displays the current weather conditions
including temperature, humidity, wind speed, and a
brief weather description.

Use the OpenWeatherMap API key from {{.ENV file WEATHER_API_KEY}}


Example usage: py -m src.main "Dallas"
**Project Summary:** A CLI application that accepts a city name and displays current weather conditions using the OpenWeatherMap API.
**Project Folder:** `output\city_weather_dashboard`

---

## Stories Completed: 3/3

### Story 1: Fetch Weather API Data — ✅ DONE

**Requirement:** Create a core module in src/weather.py that reads WEATHER_API_KEY from a .env file and fetches current weather data for a given city name from the OpenWeatherMap API, returning temperature, humidity, wind speed, and weather description as a dictionary.

**Acceptance Criteria:**
- Calling get_weather('Dallas') returns a dictionary containing keys: city, temperature, humidity, wind_speed, and description
- WEATHER_API_KEY is loaded from the .env file using python-dotenv
- Function returns correct values matching the OpenWeatherMap API response for a valid city name

**QA Status:** PASS
**Tech Stack:** See requirements.txt

---

### Story 2: Format Weather Output — ✅ DONE

**Requirement:** Create a display module in src/display.py that accepts the weather dictionary from the core module and formats it into a readable multi-line CLI weather report string showing city, temperature, humidity, wind speed, and description.

**Acceptance Criteria:**
- Calling format_weather(weather_dict) returns a formatted string containing city name, temperature, humidity, wind speed, and description
- Output is human-readable with labeled fields

**QA Status:** PASS
**Tech Stack:** See requirements.txt

---

### Story 3: Build CLI Entry Point — ✅ DONE

**Requirement:** Create src/main.py as the CLI entry point that accepts a city name as a command-line argument, calls the weather fetch function, and prints the formatted weather report to the console.

**Acceptance Criteria:**
- Running py -m src.main "Dallas" prints a formatted weather report for Dallas to the console
- Running py -m src.main with no arguments prints a usage error message
- The CLI exits cleanly after displaying the weather report

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
