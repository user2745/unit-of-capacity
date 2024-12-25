# modules/processing.py
def process_data(raw_data):
    return {k: round(v, 2) for k, v in raw_data.items()}
