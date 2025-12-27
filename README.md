# My Secret Santa simple API

Simple Secret Santa API built with FastAPI, Docker, and Poetry

## Local Development

1. Install Poetry: https://python-poetry.org/docs/#installation
2. Install dependencies: `poetry install`
3. Run application: `poetry run uvicorn app.main:app --reload`

## Docker Usage

Build image:
```bash
docker build -t secret-santa-app .