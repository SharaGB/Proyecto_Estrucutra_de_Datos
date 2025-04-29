import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    """
    Establishes a connection to the PostgreSQL database using credentials from environment variables.

    Returns:
        conn: A connection object to the PostgreSQL database.
    """
    try:
        conn = psycopg2.connect(
            dbname=config('DB_NAME'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            host=config('DB_HOST'),
            port=config('DB_PORT')
        )
        return conn
    except DatabaseError as e:
        print(f"Error connecting to the database: {e}")
