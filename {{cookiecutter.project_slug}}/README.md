# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Development Requirements

- Python3.8.2
- Pip
- Poetry (Python Package Manager)

### M.L Model Environment

```sh
MODEL_PATH={{cookiecutter.machine_learn_model_path}}
MODEL_NAME={{cookiecutter.machine_learn_model_name}}
```

### Update `/predict`

To update your machine learning model, add your `load` and `method` [change here](app/api/routes/predictor.py#L13) at `predictor.py`

## Installation

```sh
python -m venv venv
source venv/bin/activate
make install
```

## Runnning Localhost

`make run`

## Deploy app

`make deploy`

## Running Tests

`make test`

## Runnning Easter Egg

`make easter`

## Access Swagger Documentation

> <http://localhost:8080/docs>

## Access Redocs Documentation

> <http://localhost:8080/redoc>

## Project structure

Files related to application are in the `app` or `tests` directories.
Application parts are:

    app
    ├── rooter           - web routes.
    ├── controller       - application configuration, startup events, logging.
    ├── mddleware        - 
    ├── service          - logic that is not just crud related.
    ├── entity_service   - logic or sevice models for this application. 
    ├── entity           - physical models from database.
    ├── main.py          - FastAPI application creation and configuration.
    │
    doc
    ├── .gitignore
    ├── openapi.ym       - documentation for this project
    │
    docker               
    ├── docker-compose.yml
    ├──
    tests                
    ├─ unit              - unit tests
    ├─ integration       - integration tests
    ├─ e2e               - end to end tests
    ├─ _data 
    │
    Readme.md
    │
    Makefile
    │
    Dockerfile
