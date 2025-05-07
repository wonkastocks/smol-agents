# ollama_test.py
# A simple test script to verify connectivity with a local Ollama instance

import requests
import sys

OLLAMA_URL = 'http://localhost:11434'


def get_models():
    """
    Retrieves available models from a local Ollama instance.
    
    Returns:
        list: A list of available model objects, each containing name and other metadata
    """
    resp = requests.get(f"{OLLAMA_URL}/api/tags")
    resp.raise_for_status()
    models = resp.json().get('models', [])
    return models


def run_prompt(model_name, prompt="Say hello!"):
    """
    Sends a prompt to the specified Ollama model and returns the response.
    Handles streaming response from the Ollama API.
    
    Args:
        model_name (str): Name of the model to use (e.g., "phi:latest")
        prompt (str): Text prompt to send to the model
        
    Returns:
        str: The model's response text
    """
    resp = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": model_name,
            "prompt": prompt,
        },
        stream=True
    )
    resp.raise_for_status()
    responses = []
    for line in resp.iter_lines():
        if line:
            try:
                data = line.decode('utf-8')
                import json
                obj = json.loads(data)
                chunk = obj.get('response', '')
                if chunk:
                    responses.append(chunk)
                    print(f"Chunk: {chunk}")
            except Exception as e:
                print(f"Failed to parse line: {line}, error: {e}")
    return ''.join(responses)


def main():
    """
    Main function to test the Ollama connection.
    - Gets available models
    - Uses the last available model to run a test prompt
    - Prints the response
    """
    try:
        models = get_models()
        if not models:
            print("No models found on local Ollama instance.")
            sys.exit(1)
        # Use the last model in the list (as a proxy for 'last that worked')
        model = models[-1]['name']
        print(f"Testing model: {model}")
        response = run_prompt(model)
        print("Model response:", response)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
