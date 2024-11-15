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

export PYTHONPATH=.