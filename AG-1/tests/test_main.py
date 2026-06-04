import pytest
from unittest.mock import patch, MagicMock
from src.main import parse_arguments, main

def test_parse_arguments():
    """Test argument parsing with zip code"""
    with patch('sys.argv', ['main.py', '12345']):
        zipcode = parse_arguments()
        assert zipcode == '12345'

@patch('src.main.get_hourly_forecast')
@patch('src.main.parse_arguments')
def test_main_success(mock_parse, mock_forecast):
    """Test successful main execution"""
    mock_parse.return_value = '12345'
    mock_forecast.return_value = "Time | Temp | Conditions\nTest forecast"
    
    result = main()
    assert result == 0
    mock_parse.assert_called_once()
    mock_forecast.assert_called_once_with('12345')

@patch('src.main.parse_arguments')
def test_main_error(mock_parse):
    """Test main with error handling"""
    mock_parse.side_effect = Exception("Test error")
    result = main()
    assert result == 1