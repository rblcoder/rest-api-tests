# rest-api-tests

## Virtual environment
```
virtualenv venv

source venv/bin/activate

pip install -r requirements.txt
```


## Run the fast api app
```
export PYTHONPATH=.

fastapi dev src/main.py
```

## Run the tests with coverage
```
coverage run -m pytest
coverage report -m --omit="*/test*"
```

## Generate html report
```
coverage html
```

## Exclude tests folder
```
coverage html --omit="*/test*" -d tests/coverage
```

## Access the docs by adding redoc or docs# to url

## Additional info

https://sqlpad.io/tutorial/absolute-vs-relative-python-imports/

https://stackoverflow.com/questions/78505239/fastapi-app-throws-modulenotfound-error-on-startup

https://medium.com/@navinsharma9376319931/mastering-fastapi-crud-operations-with-async-sqlalchemy-and-postgresql-3189a28d06a2

export PYTHONPATH=.

## Sample .env

DATABASE_URL="sqlite:///./test.db"

## Alembic

alembic init alembic

alembic init alembic -t async migrations

alembic revision --autogenerate -m "Initial migration"

alembic upgrade head

