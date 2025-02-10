# Langgraph Project

A project for building conversational AI workflows using Langgraph.

## Installation

```bash
Clone the repository
git clone https://github.com/hulk-pham/LangGraph-AI-Agent.git
cd langgraph-project
Install dependencies
pip install -r requirements.txt
```

```bash
bash
export OPENAI_API_KEY="your-api-key"
```

## Usage

```bash
# Create virtual environment
python3.12 -m venv .venv 
source .venv/bin/activate

# Install dependencies
pip install -e .  

# Set environment variables
export PATH=$PATH:/usr/local/mysql/bin

# Run the main script
python3 src/ai_core/main.py
```

## Features

- Multi-agent conversations
- Dynamic workflow orchestration
- Custom agent behaviors
- State management

## Project Structure
├── agents/ # Agent definitions
├── graphs/ # Workflow graphs
├── utils/ # Helper functions
├── main.py # Entry point
└── requirements.txt

## Requirements

- Python 3.9+
- OpenAI API key

## Contributing

Pull requests are welcome. For major changes, please open an issue first.

## License

[MIT](LICENSE)