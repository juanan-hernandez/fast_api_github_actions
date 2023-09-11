# fast_api_github_actions

## Local setup

### Previous requirements:
**Poetry**
> curl -sSL https://install.python-poetry.org | python3 -

**pre-commit**
> brew install pre-commit

or
> pip install pre-commit


### Run tests
```bash
pytest -v -s
```

### Run app without Docker
```bash
poetry install
export PYTHONPATH=$(pwd)/app
uvicorn main:app --reload
```

### Run app with Docker
```bash
docker build -t fastapi .
docker run -p 80:80 fastapi
```
