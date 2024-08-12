# Setup ETL Project

This project corresponds to a Medium article where we discuss building an ETL pipeline using Python and PostgreSQL. You can find the full article here: [Medium Article Link]()

## Getting Started

To set up the environment, you can run the databases, Alembic migrations, and API using Docker. This ensures everything is correctly configured and ready for the ETL process.

```bash
docker-compose up --build
```

## Running the ETL

Once the environment is set up, you can run the complete ETL pipeline by installing the dependencies with Poetry and executing the ETL script.

```bash
poetry install
poetry run python scripts/etl.py
```

This will trigger the ETL process, which extracts, transforms, and loads the data into the PostgreSQL database.
