# Web Search with Ollama

This repository contains tools for performing web searches using DuckDuckGo and processing results with a local Ollama LLM instance. The project demonstrates a lightweight approach to web search using Python.

## Features

- Connect to a local Ollama instance
- Perform web searches using DuckDuckGo
- Display formatted search results

## Prerequisites

- Python 3.10+
- Local Ollama server running (with phi model or another model of your choice)
- Internet connection for web searches

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/wonkastocks/smol-agents.git
cd smol-agents
```

2. **Install dependencies**

```bash
pip install requests duckduckgo-search
```

## Project Structure

- `ollama_connect.py`: Core module for connecting to a local Ollama server
- `ollama_test.py`: Simple test script to verify Ollama connection
- `simple_web_search.py`: Standalone web search implementation using DuckDuckGo

## Usage

### Basic Ollama Test

```bash
python ollama_test.py
```

### Running Web Searches

```bash
python simple_web_search.py
```

You can modify the search queries in the `simple_web_search.py` file to search for different topics.

## Use Cases

- Research tool for gathering current information from the web
- Foundation for building more complex search tools
- Educational reference for integrating search capabilities in other projects

## License

MIT
