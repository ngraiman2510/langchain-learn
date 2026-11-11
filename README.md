# LangChain + LangSmith example

This script sends three prompts to OpenAI using LangChain. If LangSmith tracing is enabled, the runs are also recorded in your LangSmith project.

## Setup

Use Python 3.10 or later. From this folder, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
python -m pip install langchain-openai python-dotenv
```

Create a `.env` file in this folder:

```env
OPENAI_API_KEY=your_openai_api_key
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT="LangChain learning"
```

`OPENAI_API_KEY` is required. LangSmith settings are optional; omit them if you don't want tracing. Never commit real API keys.

## Run

```bash
python traced_app.py
```

The script uses the `gpt-4o-mini` model. API usage may incur charges.
