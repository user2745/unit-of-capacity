from modules.data_ingestion import fetch_data
from modules.processing import process_data_with_ollama

class CoreEngine:
    def __init__(self, fetch_endpoint, log_endpoint=None):
        self.fetch_endpoint = fetch_endpoint
        self.log_endpoint = log_endpoint

    def run(self):
        # Step 1: Fetch data
        raw_data = fetch_data(self.fetch_endpoint)
        bitcoin_price = raw_data["data"]["bitcoin"]["usd"]

        # Step 2: Process data using the LLM
        insights = process_data_with_ollama(raw_data["data"])

        # Step 3: Format and return structured output
        structured_summary = self.format_output(bitcoin_price, insights)
        return structured_summary

    @staticmethod
    def format_output(price, insights):
        return f"""
Bitcoin Analysis:
Price: ${price:,} USD
Insight: {insights}
"""
