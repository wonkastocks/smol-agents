# simple_search.py
# Basic implementation of web search using DuckDuckGo and Ollama for processing

import requests
import sys
import json

# DuckDuckGo search function
def duckduckgo_search(query):
    """
    Performs a basic search using DuckDuckGo's API.
    
    Args:
        query (str): The search query string
        
    Returns:
        dict: Raw JSON response from DuckDuckGo
    """
    print(f"Searching DuckDuckGo for: {query}")
    search_url = "https://duckduckgo.com/"
    params = {
        'q': query,
        'format': 'json'
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(search_url, params=params, headers=headers)
        response.raise_for_status()
        results = response.json()
        return results
    except Exception as e:
        print(f"Search error: {e}")
        return None

# Ollama API connection
def ask_ollama(prompt, model="phi:latest"):
    """
    Sends a prompt to a local Ollama instance and gets the response.
    
    Args:
        prompt (str): The text prompt to send to Ollama
        model (str): The model name to use (default: "phi:latest")
        
    Returns:
        str: The model's text response
    """
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        print(f"Ollama API error: {e}")
        return None

def main():
    """
    Main function that demonstrates the end-to-end process:
    1. Search for information using DuckDuckGo
    2. Process the results with a local Ollama model
    3. Display the analysis
    """
    # The query for NFL teams
    query = "top NFL teams predictions 2025 season AFC NFC"
    
    # Get search results
    search_results = duckduckgo_search(query)
    
    if not search_results:
        print("Could not get search results")
        return
    
    # Extract useful information from search
    result_text = json.dumps(search_results, indent=2)[:2000]  # Truncate to avoid large output
    print("\nSearch results (truncated):")
    print(result_text)
    
    # Ask Ollama to analyze and summarize the results
    prompt = f"""Based on these search results about the top NFL teams for the 2025 season, 
    list which teams are predicted to be the best in both the NFC and AFC conferences.
    Present your answer in a clear list format, separated by conference.
    
    Search results: {result_text}
    """
    
    analysis = ask_ollama(prompt)
    
    if analysis:
        print("\nAnalysis from Ollama:")
        print(analysis)
    else:
        print("Could not get analysis from Ollama")

if __name__ == "__main__":
    main()
