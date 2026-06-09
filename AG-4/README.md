# Weather CLI

A command-line tool to fetch current weather and a 5-day forecast for any city.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and add your OpenWeatherMap API key:
   ```bash
   cp .env.example .env
   ```

3. Edit `.env` and set your API key:
   ```
   WEATHER_API_KEY=your_actual_api_key_here
   ```

## Usage

```bash
py -m src.main London
```

Example output:
```
Current Weather for London, GB:
  Clear sky
  Temperature: 15.0°C (Feels like 13.0°C)
  Humidity: 80%
  Wind Speed: 3.5 m/s
5-Day Forecast:
  2024-01-01: Cloudy, 14.0°C
  2024-01-02: Rain, 12.0°C
```

## Run Tests

```bash
pytest tests/
```