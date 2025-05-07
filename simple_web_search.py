# simple_web_search.py
# A standalone web search implementation using DuckDuckGo search

from duckduckgo_search import DDGS

def search_web(query, max_results=5):
    """
    Search the web using DuckDuckGo search API.
    
    Args:
        query (str): The search query to send to DuckDuckGo
        max_results (int): Maximum number of results to return
        
    Returns:
        list: A list of search result dictionaries containing title, body, and href
    """
    print(f"Searching for: {query}")
    try:
        # Create a DuckDuckGo search session
        with DDGS() as ddgs:
            # Perform the text search and convert results to a list
            results = list(ddgs.text(query, max_results=max_results))
            return results
    except Exception as e:
        # Handle any errors that occur during the search
        print(f"Error searching: {e}")
        return []

def main():
    """
    Main function to demonstrate web search functionality.
    
    This function:
    1. Defines an initial search query
    2. Performs the search
    3. If no results are found, tries a fallback query
    4. Displays the search results in a formatted manner
    """
    # Initial search query
    query = "top NFL teams predictions 2025 season AFC NFC"
    results = search_web(query)
    
    # Try a fallback query if the first one returns no results
    if not results:
        print("No search results found. Trying alternative query...")
        results = search_web("2025 NFL season predictions top teams")
    
    # Display results if found
    if results:
        print("\n===== SEARCH RESULTS =====\n")
        for i, result in enumerate(results, 1):
            print(f"Result {i}:")
            print(f"Title: {result.get('title')}")
            print(f"Content: {result.get('body')}")
            print(f"URL: {result.get('href')}")
            print()
    else:
        print("Could not find any search results.")

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
