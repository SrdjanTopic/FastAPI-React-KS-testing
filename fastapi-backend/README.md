# FastAPI initial project

## Content

### Follow these steps to start the application:

1. install poetry
2. poetry shell
3. poetry add $( cat requirements.txt )
4. cd app
5. uvicorn main:app --reload

### Alembic commands:

1. alembic revision --autogenerate -m "<revision_message>"
2. alembic upgrade head

### Generate requirements.txt:

1. poetry export -f requirements.txt --output requirements.txt --without-hashes --without-urls
