# rest-api-tests

## Run the tests with coverage

coverage run -m pytest
coverage report -m

## Generate html report
coverage html

## Exclude tests folder
coverage html --omit="*/test*" -d tests/coverage