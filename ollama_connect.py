#!/usr/bin/env python3
"""
Ollama Connection Module

This module provides functions to connect to a local Ollama instance,
retrieve available models, and run prompts against specified models.
It handles the API communication and response processing.

Author: wonkastocks
Date: May 2025
"""

import requests
import json

# Base URL for Ollama API - modify if your Ollama instance is running elsewhere
OLLAMA_URL = 'http://localhost:11434'

def get_models():
    """
    Retrieves available models from a local Ollama instance.
    
    This function queries the Ollama API to get a list of all available models
    that have been downloaded and are ready to use.
    
    Returns:
        list: A list of available model objects, each containing name and other metadata
              such as model size, modified time, and other properties.
    
    Raises:
        requests.exceptions.RequestException: If there's a communication error with the Ollama API
    """
    resp = requests.get(f"{OLLAMA_URL}/api/tags")
    resp.raise_for_status()  # Raise an exception for HTTP errors
    models = resp.json().get('models', [])  # Extract the models list, defaulting to empty list
    return models


def run_prompt(model_name, prompt="Say hello!"):
    """
    Sends a prompt to the specified Ollama model and returns the response.
    
    This function handles communication with the Ollama API, sending the prompt
    and processing the streaming response. It aggregates all response chunks
    into a single text string.
    
    Args:
        model_name (str): Name of the model to use (e.g., "phi:latest")
        prompt (str): Text prompt to send to the model
        
    Returns:
        str: The model's complete response text
    
    Raises:
        requests.exceptions.RequestException: If there's a communication error with the Ollama API
    """
    # Configure the API request with streaming enabled
    resp = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": model_name,  # Specify which model to use
            "prompt": prompt,     # The text prompt to send
        },
        stream=True  # Enable streaming for token-by-token response
    )
    resp.raise_for_status()  # Raise an exception for HTTP errors
    
    # Process the streaming response
    responses = []  # List to collect response chunks
    for line in resp.iter_lines():
        if line:  # Skip empty lines
            try:
                # Decode and parse the JSON response
                data = line.decode('utf-8')
                obj = json.loads(data)
                
                # Extract the response text chunk
                chunk = obj.get('response', '')
                if chunk:
                    responses.append(chunk)  # Add to response collection
            except Exception as e:
                print(f"Failed to parse line: {line}, error: {e}")
    
    # Combine all response chunks into a single string
    return ''.join(responses)
