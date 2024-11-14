# rest-api-tests

## Run the fast api app
```
fastapi dev main.py
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

## Access the docs by adding redoc or docs to url


## Virtual environment

virtualenv venv

source venv/bin/activate

