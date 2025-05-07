# direct_question.py
# Direct question answering using Ollama without web search

import requests

# Function to ask Ollama a question
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
    Main function that demonstrates direct question answering with Ollama.
    - Creates a detailed prompt
    - Sends it to Ollama
    - Displays the response
    
    Note: The response quality depends on the model's knowledge cutoff date.
    For current information, use the web search scripts instead.
    """
    # Direct question to the model
    prompt = """
    I need a prediction for the top NFL teams for the 2025-2026 season.
    
    Please list the top 5 teams that are likely to be contenders in each conference (NFC and AFC).
    Format your answer like this:
    
    NFC TOP TEAMS:
    1. [Team name] - [Brief reason based on current roster, coaching staff, and recent performance]
    2. [Team name] - [Brief reason]
    3. [Team name] - [Brief reason]
    4. [Team name] - [Brief reason]
    5. [Team name] - [Brief reason]
    
    AFC TOP TEAMS:
    1. [Team name] - [Brief reason based on current roster, coaching staff, and recent performance]
    2. [Team name] - [Brief reason]
    3. [Team name] - [Brief reason]
    4. [Team name] - [Brief reason]
    5. [Team name] - [Brief reason]
    """
    
    # Get response from Ollama
    print("Asking local Ollama model (phi) for NFL predictions...")
    response = ask_ollama(prompt)
    
    if response:
        print("\n===== NFL TEAM PREDICTIONS FOR 2025-2026 SEASON =====\n")
        print(response)
    else:
        print("Failed to get a response from Ollama")

if __name__ == "__main__":
    main()
