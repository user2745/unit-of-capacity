# main.py
from engine.core_engine import CoreEngine

if __name__ == "__main__":
    fetch_url = "http://127.0.0.1:5000/fetch"
    process_url = "http://127.0.0.1:5000/process"
    log_url = "http://127.0.0.1:5000/log"

    engine = CoreEngine(fetch_url, process_url, log_url)
    engine.run()
