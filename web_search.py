# web_search.py
# Implementation of web search using BeautifulSoup for HTML parsing

import requests
import sys
from bs4 import BeautifulSoup

# Function to perform a web search and get relevant results
def web_search(query):
    """
    Performs a web search using Google and parses the HTML results.
    
    Args:
        query (str): The search query to submit
        
    Returns:
        list: A list of dictionaries containing title, snippet, and link for each result
    """
    print(f"Searching for: {query}")
    search_url = "https://www.google.com/search"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    params = {'q': query}
    
    try:
        response = requests.get(search_url, params=params, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract search result titles and snippets
        results = []
        for result in soup.select('.g'):
            title_elem = result.select_one('h3')
            snippet_elem = result.select_one('.VwiC3b')
            link_elem = result.select_one('a')
            
            if title_elem and snippet_elem and link_elem:
                title = title_elem.get_text()
                snippet = snippet_elem.get_text()
                link = link_elem.get('href')
                if link and link.startswith('/url?q='):
                    link = link.split('/url?q=')[1].split('&sa=')[0]
                
                results.append({
                    'title': title,
                    'snippet': snippet,
                    'link': link
                })
        
        return results
    except Exception as e:
        print(f"Search error: {e}")
        return []

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
    1. Search for NFL team predictions
    2. Fall back to ESPN if no results
    3. Format search results for Ollama
    4. Get and display analysis from Ollama
    """
    # Search for NFL team predictions
    query = "top NFL teams predictions 2025 season AFC NFC championship contenders"
    search_results = web_search(query)
    
    if not search_results:
        # Try ESPN or other sports sites directly
        search_results = web_search("ESPN NFL power rankings 2024 2025 season predictions")
    
    if not search_results:
        print("Could not get any search results")
        return
    
    # Format search results for the prompt
    formatted_results = "\n\n".join([f"Title: {r['title']}\nSnippet: {r['snippet']}\nLink: {r['link']}" for r in search_results[:5]])
    
    # Create a prompt for Ollama
    prompt = f"""
    Based on these search results about NFL team predictions for the 2025 season:
    
    {formatted_results}
    
    Please list the top 5 teams that are likely to be contenders in each conference (NFC and AFC) for the 2025 NFL season.
    Format your answer like this:
    
    NFC TOP TEAMS:
    1. [Team name] - [Brief reason]
    2. [Team name] - [Brief reason]
    ...
    
    AFC TOP TEAMS:
    1. [Team name] - [Brief reason]
    2. [Team name] - [Brief reason]
    ...
    """
    
    # Get analysis from Ollama
    analysis = ask_ollama(prompt)
    
    if analysis:
        print("\n===== NFL TEAM PREDICTIONS FOR 2025 SEASON =====\n")
        print(analysis)
    else:
        print("Failed to get analysis from Ollama")

if __name__ == "__main__":
    main()
