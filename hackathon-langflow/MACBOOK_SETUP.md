## MacBook Setup Instructions

### Installing Langflow with `uv`

1. Make sure you have Python 3.10+ installed on your MacBook
2. Install `uv` if you don't have it yet:
   ```bash
   curl -sSf https://install.update.dev | python3

uv pip install langflow

# Create a virtual environment
uv venv .venv-langflow

# Activate the environment
source .venv-langflow/bin/activate

git clone https://github.com/yourusername/sec-edgar-via-mcp-browserbase.git
cd sec-edgar-via-mcp-browserbase
git checkout hackathon/langflow-edgar-agent

uv pip install -r hackathon-langflow/requirements.txt

uv run langflow run

The Langflow UI should now be accessible at http://127.0.0.1:7860

Note About Python Versions
This project was originally developed in RHEL9 with Python 3.9
Langflow requires Python 3.10+
The MacBook development environment uses Python 3.11
The core SEC EDGAR client code is compatible with all Python versions 3.9+
Troubleshooting Langflow Installation
If you encounter issues with Langflow installation:

Try reinstalling with force:

If you see "No module named 'langflow.main'", use:

For dependency resolution issues, clear your pip cache:

For more details, see the Langflow installation documentation


