FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y build-essential

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false 

RUN poetry install --no-interaction --no-ansi

COPY . /app

EXPOSE 8000

ENV ENVIRONMENT=production

CMD ["python", "-m", "setup_small_project"]
