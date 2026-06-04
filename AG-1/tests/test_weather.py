import pytest
from unittest.mock import patch, MagicMock
from src.weather import get_weather_by_zip

def test_get_weather_by_zip_success():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'name': 'Beverly Hills',
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 295.15, 'humidity': 65}
    }
    
    with patch('requests.get', return_value=mock_response):
        result = get_weather_by_zip('90210', 'test_api_key')
        assert result['name'] == 'Beverly Hills'
        assert result['weather'][0]['description'] == 'clear sky'

def test_get_weather_by_zip_invalid_api_key():
    mock_response = MagicMock()
    mock_response.status_code = 401
    
    with patch('requests.get', return_value=mock_response):
        with pytest.raises(ValueError, match="Invalid API key"):
            get_weather_by_zip('90210', 'invalid_key')