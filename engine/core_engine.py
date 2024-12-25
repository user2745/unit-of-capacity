# engine/core_engine.py
from modules.data_ingestion import fetch_data
from modules.processing import process_data
from modules.logging import log_data

class CoreEngine:
    def __init__(self, fetch_endpoint, process_endpoint, log_endpoint):
        self.fetch_endpoint = fetch_endpoint
        self.process_endpoint = process_endpoint
        self.log_endpoint = log_endpoint

    def run(self):
        # Step 1: Fetch data
        raw_data = fetch_data(self.fetch_endpoint)
        print(f"Fetched Data: {raw_data}")

        # Step 2: Process data
        processed_data = process_data(raw_data["data"])
        print(f"Processed Data: {processed_data}")

        # Step 3: Log data
        log_data(processed_data)
