import pandas as pd

class DataProcessor:
    def __init__(self, raw_data_dir="data/finance/raw", processed_data_dir="data/finance/processed"):
        self.raw_data_dir = raw_data_dir
        self.processed_data_dir = processed_data_dir

    def process_data(self, raw_data):
        """
        Process and clean raw financial data.
        """
        rows = []
        for timestamp, values in raw_data.items():
            rows.append({
                "timestamp": timestamp,
                "open": float(values["1. open"]),
                "high": float(values["2. high"]),
                "low": float(values["3. low"]),
                "close": float(values["4. close"]),
                "volume": int(values["5. volume"]),
            })
        df = pd.DataFrame(rows)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df

    def save_data(self, df, filename):
        """
        Save processed data to a CSV file.
        """
        filepath = f"{self.processed_data_dir}/{filename}"
        df.to_csv(filepath, index=False)
        print(f"Processed data saved to {filepath}")
