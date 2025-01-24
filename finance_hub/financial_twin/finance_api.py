################################################################################
###                                                                          ###
### Created by Mahdi Manoochertayebi 2025-2026                               ###
###                                                                          ###
################################################################################

import requests

################################################################################

class FinanceAPI:
    def __init__(self, api_key, base_url="https://www.alphavantage.co/query"):
        self.api_key = api_key
        self.base_url = base_url

    def fetch_stock_data(self, symbol, interval="1min"):
        """
        Fetch real-time stock data from the Alpha Vantage API.
        """
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": interval,
            "apikey": self.api_key,
            "datatype": "json",
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if f"Time Series ({interval})" in data:
                return data[f"Time Series ({interval})"]
            else:
                raise ValueError("No data found in API response.")
        else:
            raise ConnectionError(f"API request failed with status code {response.status_code}")
