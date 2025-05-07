# Web Search with SMOL Agents

This repository contains a collection of tools for performing web searches using the `smolagents` library and Ollama for local LLM processing. The project demonstrates how to interface with a local Ollama server, perform web searches, and analyze results using AI models locally.

## Features

- Connect to a local Ollama instance
- Perform web searches using DuckDuckGo
- Process search results with local AI models
- Various implementations from basic to advanced

## Prerequisites

- Python 3.10+
- Local Ollama server running (with phi model or another model of your choice)
- Internet connection for web searches

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/web-search-with-smol.git
cd web-search-with-smol
```

2. **Create and activate a virtual environment (recommended)**

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

## Project Structure

- `ollama_connect.py`: Basic module for connecting to a local Ollama server
- `ollama_test.py`: Simple test script to verify Ollama connection
- `simple_search.py`: Basic web search using DuckDuckGo and Ollama
- `simple_web_search.py`: Standalone web search without LLM processing
- `smol_agent.py`: Integration with smolagents for advanced agent-based searching
- `web_search.py`: Web search implementation with BeautifulSoup
- `direct_question.py`: Direct question answering with Ollama

## Usage

### Basic Ollama Test

```bash
python ollama_test.py
```

### Simple Web Search

```bash
python simple_web_search.py
```

### Using SMOL Agent

```bash
python smol_agent.py
```

## Use Cases

- Research tool for current information using local AI resources
- Integration example for building more complex agent-based applications
- Educational resource for understanding AI agent development

## Dependencies

See `requirements.txt` for a complete list of dependencies.

## License

MIT
