# smol_agent.py
# Integration of smolagents with local Ollama for web search

import os
from smolagents import ToolCallingAgent, DuckDuckGoSearchTool, LiteLLMModel, CodeAgent

# Configure LiteLLM for debug output
os.environ['LITELLM_LOG_LEVEL'] = 'INFO'

def main():
    """
    Main function that demonstrates using smolagents with Ollama.
    
    This script sets up a ToolCallingAgent with DuckDuckGoSearchTool, using
    a local Ollama model through LiteLLM for backend processing.
    """
    print("Setting up the agent with Ollama...")

    # Configure LiteLLM to use Ollama
    # The 'ollama/' prefix tells LiteLLM to use the Ollama provider
    model = LiteLLMModel(
        model_id="ollama/phi:latest",  # Using ollama/ prefix for LiteLLM
        api_base="http://localhost:11434", # Ollama server address
        temperature=0.7,  # Control creativity/randomness
    )

    # Create the agent with DuckDuckGo search capability
    # ToolCallingAgent is simpler than CodeAgent for basic web searching
    agent = ToolCallingAgent(
        tools=[DuckDuckGoSearchTool()], 
        model=model
    )

    # Define the search query
    print("Running agent to find NFL championship predictions...")
    query = "Who are going to be the top NFL teams in the 2025 season? List the best teams in both NFC and AFC."
    
    # Run the agent with the query
    result = agent.run(query)
    
    # Print results
    print("\nFINAL RESULT:\n")
    print(result)


if __name__ == "__main__":
    main()
