# Multiagent system 



## ◻️ Setup 

◽  **Step 1** Install [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)

◽  **Step 2**  Create a virtual environment

```bash
uv venv .venv 
```

◽  **Step 3** Create a new Python project.

```bash
uv init
```

◽  **Step 4** Install packages into the current environment.

If you have a pyproject.toml file with all the dependencies. Just run and the environment will be ready

```bash
uv pip install -e .
```

If not, you can add and remove dependencies with this command lines:

```bash
uv add: Add a dependency to the project.
```

```bash
uv remove: Remove a dependency from the project.
```

Other helpful commands

Sync the project's dependencies with the environment

```bash
uv sync 
```

Create a lockfile for the project's dependencies.

```bash
uv lock
```

View the dependency tree for the project.

```bash
uv tree
```

## ◻️ Usage
```bash
uv run main.py
```

## ◻️ Documentation
To visualize the sqlite database, you can use the [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer)


## ◻️ Deploy 

Build the project into distribution archives.

```bash
uv build 
```

