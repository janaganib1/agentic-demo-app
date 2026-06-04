# Weather Forecast CLI

A simple command-line tool to get hourly weather forecasts for US zip codes.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Get an API key from OpenWeatherMap (https://openweathermap.org/api)

3. Copy `.env.example` to `.env` and add your API key:
```bash
cp .env.example .env
```

4. Edit `.env` and replace `your_api_key_here` with your actual API key

## Usage

Run with a US zip code:
```bash
py -m src.main 12345
py -m src.main 90210
```

## Example Output

```
Hourly Weather Forecast for 12345:

Time            Temp     Conditions
--------------------------------------------------
2024-01-15 12:00 45°F     Clear Sky
2024-01-15 15:00 48°F     Few Clouds
2024-01-15 18:00 42°F     Scattered Clouds
...
```

## Testing

Run tests with:
```bash
pytest tests/