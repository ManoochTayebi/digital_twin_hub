################################################################################
###                                                                          ###
### Created by Mahdi Manoochertayebi 2025-2026                               ###
###                                                                          ###
################################################################################

import time

import financial_twin as ft
################################################################################

class TradingDataPipeline:
    def __init__(self, api_key, symbol, interval="1min", duration=60):
        self.api = ft.FinanceAPI(api_key)
        self.symbol = symbol
        self.interval = interval
        self.duration = duration
        self.processor = ft.DataProcessor()

    def run(self):
        """
        Execute the pipeline: fetch, process, and save data.
        """
        start_time = time.time()
        while time.time() - start_time < self.duration:
            print(f"Fetching data for {self.symbol}...")
            try:
                raw_data = self.api.fetch_stock_data(self.symbol, self.interval)
                df = self.processor.process_data(raw_data)
                filename = f"{self.symbol}_data.csv"
                self.processor.save_data(df, filename)
            except Exception as e:
                print(f"Error during pipeline execution: {e}")
            time.sleep(60)  # Wait for the next interval
