from engine.core_engine import CoreEngine

def generate_bitcoin_insights():
    fetch_url = "http://127.0.0.1:5000/fetch"
    log_url = None  # Optional logging endpoint, not used here

    # Initialize the engine
    engine = CoreEngine(fetch_url, log_url)

    # Run the engine and return the insights
    return engine.run()

if __name__ == "__main__":
    insights = generate_bitcoin_insights()
    print(insights)
