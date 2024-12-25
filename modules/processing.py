import requests

# modules/processing.py
def process_data(raw_data):
    return {k: round(v, 2) for k, v in raw_data.items()}

def process_data_with_ollama(data):
    # Prepare data for the LLM
    prompt = f"Analyze the following market data and provide a concise summary of key insights.  Keep it less than 3 sentences.:\n{data}"

    # Call the local Ollama LLM
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "phi3",  # Replace with the actual model name (e.g., "llama-3-8b")
                "system": "You are a financial analyst.",  # System role setting
                "messages": [{"role": "user", "content": prompt}],
                "stream": False,
            }
        )
        response.raise_for_status()  # Raise error for HTTP issues
        llm_output = response.json()
        
        return llm_output.get("message", {}).get("content", "No insights generated.")
    except Exception as e:
        return f"Error processing data with LLM: {e}"