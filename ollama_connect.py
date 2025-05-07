# ollama_connect.py
# Core module for connecting to a local Ollama instance and running prompts

import requests

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
            except Exception as e:
                print(f"Failed to parse line: {line}, error: {e}")
    return ''.join(responses)
