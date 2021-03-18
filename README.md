# FastApi BoilerPlate
Repo is useful for simple and fast development to production with FastApi. Framework is the one of the asynchronous framework for Python, for documation please refer to [FastAPI](https://fastapi.tiangolo.com/)

## Notes
FastAPI boilerplate supports Python version 3.8 and above.
This boilerplate is using [Gino-ORM](https://python-gino.org/) for database connections, [Poetry](https://python-poetry.org/docs/) for packaging and Docker file for non-root user.

In order to use boilerplate  for development we suggest you followings:
### 🕹 Guide

##### You can either use poetry or pip itself

For development with poetry:

```sh
poetry shell

poetry install

```

For development with pip:
```sh
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

Check this file and modife accordingly .env

```sh

source .env

```

For database migrations:
```
alembic revision --autogenerate

alembic upgrade heads
```
Last but not the least do the followings the you are ready to go:
```
uvicorn app.main:app --reload

add .env to gitignore

rm -rf .git
```


##  Contributing
Fell free to open issue and send pull request.

## Supported OS
Linux, MacOS
