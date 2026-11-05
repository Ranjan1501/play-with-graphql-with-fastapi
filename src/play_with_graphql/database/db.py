import os
import logging

import psycopg
from dotenv import load_dotenv

# Read environment variables from the project-root .env file.
load_dotenv()

logger = logging.getLogger(__name__)

# Read database configuration from environment variables.
DB_CONFIG = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": os.getenv("POSTGRES_PORT", "5432"),
    "dbname": os.getenv("POSTGRES_DB", "graphql_learning"),
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", ""),
}

# Tracks successful SQL executions during our experiment.
query_count = 0


def get_connection():
    """
    Create a new PostgreSQL connection.

    The caller is responsible for closing it.
    """
    return psycopg.connect(**DB_CONFIG)


def check_database_connection() -> bool:
    """
    Check whether PostgreSQL is reachable.
    """

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")

        logger.info("PostgreSQL connection successful")
        return True

    except psycopg.Error as error:
        logger.warning(
            "PostgreSQL unavailable. Using in-memory data. Reason: %s",
            error
        )
        return False


def execute_query(sql: str, params: tuple = ()):
    """
    Execute a SQL query and return all rows.

    Each call opens and closes a connection.
    This is intentionally simple for our learning exercise.
    """

    global query_count

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)

            # Count the actual SQL query execution.
            query_count += 1

            # Fetch rows only for queries that return results.
            return cursor.fetchall()


def reset_query_count():
    global query_count
    query_count = 0


def get_query_count() -> int:
    return query_count

