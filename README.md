# FastAPI Alten Test Project

## Requirements

* [Docker](https://www.docker.com/)
* [uv](https://docs.astral.sh/uv/) for Python package and environment management

## General Workflow

By default, dependencies are managed with [uv](https://docs.astral.sh/uv/). Please install it if you haven't already.

```console
$ uv sync
```

Then activate the virtual environment:

```console
$ source .venv/bin/activate
```

Make sure your editor is using the correct Python virtual environment, with the interpreter at `.venv/bin/python`.

Next, create a `.env` file based on the provided [example](.env.example).

## Development

Install pre-commit hooks:

```console
$ pre-commit install
```

### Database

For local development, you need to launch your own database. You can use the attached [docker-compose](./docker-compose.yml) file by running:

```console
$ docker compose up
```

Once your database is up and running, apply Alembic migrations. If you are using VS Code, you can use [launch.json](.vscode/launch.json) to start the development server.

Otherwise, run these commands manually:

First, apply Alembic migrations:

```console
$ alembic upgrade head
```

Next, start the Uvicorn server:

```console
$ uvicorn app.main:app
```