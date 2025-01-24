from .trading_pipeline import TradingDataPipeline

if __name__ == "__main__":
    API_KEY = "your_alpha_vantage_api_key"
    SYMBOL = "AAPL"  # Replace with the desired stock symbol
    INTERVAL = "1min"
    DURATION = 3600  # 1 hour

    pipeline = TradingDataPipeline(API_KEY, SYMBOL, INTERVAL, DURATION)
    pipeline.run()
