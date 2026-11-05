import logging

import psycopg

from play_with_graphql.database.db import execute_query
from play_with_graphql.models.user import User
from play_with_graphql.services import memory_data

logger = logging.getLogger(__name__)


def get_all_users() -> list[User]:

    try:
        # Fetch all users using one database query.
        rows = execute_query(
            "SELECT id, name, email FROM users ORDER BY id"
        )

        return [
            User(id=row[0], name=row[1], email=row[2])
            for row in rows
        ]

    except psycopg.Error as error:
        logger.warning("Could not fetch users from PostgreSQL: %s", error)

        # Fallback to in-memory data.
        return [
            User(
                id=user["id"],
                name=user["name"],
                email=user["email"]
            )
            for user in memory_data.users
        ]