#!/usr/bin/env python3
"""
Ollama Connection Test

This script tests the connection to a local Ollama instance by querying available models
and running a simple prompt. It provides visual feedback by printing response chunks
as they are received, demonstrating the streaming capabilities of the Ollama API.

Author: wonkastocks
Date: May 2025
"""

import requests  # For HTTP communication with Ollama API
import sys       # For system functions like exit codes
import json     # For JSON parsing

# Base URL for the Ollama API server - change if running on a different host/port
OLLAMA_URL = 'http://localhost:11434'


def get_models():
    """
    Retrieves available models from a local Ollama instance.
    
    This function queries the Ollama API to get a list of all available models
    that have been downloaded to the local instance.
    
    Returns:
        list: A list of available model objects, each containing name, modified time,
              size, and other metadata.
    
    Raises:
        requests.exceptions.RequestException: If there's an error communicating with the Ollama API
    """
    # Send a GET request to the Ollama tags endpoint
    resp = requests.get(f"{OLLAMA_URL}/api/tags")
    resp.raise_for_status()  # Raise exception if request failed
    
    # Extract and return the models list from the response
    models = resp.json().get('models', [])
    return models


def run_prompt(model_name, prompt="Say hello!"):
    """
    Sends a prompt to the specified Ollama model and returns the response.
    
    This function handles the streaming response from Ollama, printing each chunk
    as it arrives to provide real-time feedback. It then combines all chunks
    into a single response string.
    
    Args:
        model_name (str): Name of the model to use (e.g., "phi:latest")
        prompt (str): Text prompt to send to the model
        
    Returns:
        str: The complete model response as a string
    
    Raises:
        requests.exceptions.RequestException: If there's an error communicating with the Ollama API
    """
    # Configure the request to use streaming for real-time response
    resp = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": model_name,  # The model to use for generation
            "prompt": prompt,     # The user's prompt
        },
        stream=True  # Enable streaming to get token-by-token response
    )
    resp.raise_for_status()  # Raise exception if request failed
    
    # Process the streaming response
    responses = []  # List to collect all response chunks
    for line in resp.iter_lines():
        if line:  # Skip empty lines
            try:
                # Parse each chunk of the response
                data = line.decode('utf-8')
                obj = json.loads(data)
                chunk = obj.get('response', '')
                
                # If we got a valid chunk, add it to our collection and print it
                if chunk:
                    responses.append(chunk)
                    print(f"Chunk: {chunk}")  # Show real-time progress
            except Exception as e:
                print(f"Failed to parse line: {line}, error: {e}")
    
    # Combine all chunks into the final response
    return ''.join(responses)


def main():
    """
    Main function to test the Ollama connection.
    
    This function:
    1. Retrieves available models from the Ollama instance
    2. Selects the last model in the list (usually the most recently added)
    3. Runs a test prompt with the selected model
    4. Displays the model's response
    
    Exits with error code 1 if no models are found or if an exception occurs.
    """
    try:
        # Get the list of available models
        print("Querying available models from Ollama...")
        models = get_models()
        
        # Check if any models were found
        if not models:
            print("No models found on local Ollama instance. Please download a model first.")
            sys.exit(1)
            
        # Use the last model in the list (usually the most recently added)
        model = models[-1]['name']
        print(f"Testing model: {model}")
        
        # Run a test prompt and display the response
        response = run_prompt(model)
        print("\nComplete model response:", response)
        print("\nTest completed successfully!")
        
    except requests.exceptions.ConnectionError:
        print(f"Error: Could not connect to Ollama at {OLLAMA_URL}")
        print("Please make sure Ollama is running and accessible.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


# Only run the test if this script is executed directly
if __name__ == "__main__":
    main()
