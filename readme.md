# Read Me
This repo serves as a standard template for creating an API using fastapi that uses & connects:
- PostgreSQL -> psycopg2 as driver
- Alembic for migrations
- sqlalchemy for ORM 
- Uvicorn as web server
- FastAPI for python framework

## Running the webserver
`uvicorn app.main:app --reload`

## Creating a migration automatically 
More information can be found [here](https://alembic.sqlalchemy.org/en/latest/autogenerate.html)
`alembic revision --autogenerate -m "Added account table"`
