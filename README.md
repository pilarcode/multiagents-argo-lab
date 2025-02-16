# Multiagent system 
This is a multiagent system built using [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer) and [agno](https://docs.agno.com/).


## ◻️ Setup 

◽  **Step 1** Install [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)

◽  **Step 2**  Create a virtual environment

```bash
uv venv .venv 
```

◽  **Step 3** Install packages into the current environment.

If you have a pyproject.toml file with all the dependencies. Just run and the environment will be ready

```bash
uv pip install -e .
```

## ◻️ Usage
```bash
uv run main.py
```
Go to http://127.0.0.1:8046/