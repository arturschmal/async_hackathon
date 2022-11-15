# Fastapi REST api performance

We will run a 'realworld' example fastapi application backed by a postgres database and measure its performance.

## background

Please read the summary of a talk about Python performance monitoring at EuroPython 2022: https://ep2022.europython.eu/session/why-is-it-slow-strategies-for-solving-performance-problems

## Installation and testing steps

1. read the readme of the example app project
1. install docker including docker-compose
   - or create a local venv for the application and install postgres locally
   - current test settings are set to docker-compose routing, replace `host.docker.internal` with `localhost` if you do not use docker in app.core.settings.test.py
1. `docker-compose up -d db` starts the database container required for pytest
1. `poetry run python ./scripts/create_db.py` to create the database
1. `poetry run alembic upgrade head` to perform database migrations
1. `poetry run pytest tests` to run all unit tests
1. `docker-compose up` to start both database and app containers
1. access localhost:8000/docs for the api documentation
1. use the POST endpoint of user to create a test user and save the returned token
1. at the top of the page press "Authorize" and fill in "Token {token}" to authorize API
1. you can test the api via the swagger docs page

## Challenge

1. use the approach in ./tests/test_routes/ to create a test that measures the response times of multiple api calls
   - use the provided async client in ./tests/conftest.py
   - compute the average response time within the unit test framework
1. use py-spy to measure the performance of Python functions while running your unit test

## references

1. https://pypi.org/project/py-spy/
