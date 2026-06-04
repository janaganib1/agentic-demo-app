"""Bitcoin price fetcher module."""

import urllib.request
import json
from .config import BITCOIN_API_URL


def get_bitcoin_price() -> float:
    """Fetch current Bitcoin price in USD.
    
    Returns:
        float: Current Bitcoin price in USD
        
    Raises:
        Exception: If price fetch fails
    """
    try:
        with urllib.request.urlopen(BITCOIN_API_URL) as response:
            data = json.loads(response.read().decode())
            price_str = data['bpi']['USD']['rate'].replace(',', '').replace('$', '')
            return float(price_str)
    except Exception as e:
        raise Exception(f"Failed to fetch Bitcoin price: {e}")