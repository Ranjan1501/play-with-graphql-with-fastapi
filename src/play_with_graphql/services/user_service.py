
import logging

import psycopg

from play_with_graphql.database.db import execute_query
from play_with_graphql.models.user import User
from play_with_graphql.services import memory_data

logger = logging.getLogger(__name__)


def get_users_page(
    first: int,
    after: int | None = None,
) -> tuple[list[User], bool]:

    try:
        # Fetch one extra record to determine whether another page exists.
        cursor_id = after if after is not None else 0

        rows = execute_query(
            """
            SELECT id, name, email
            FROM users
            WHERE id > %s
            ORDER BY id
            LIMIT %s
            """,
            (cursor_id, first + 1),
        )

        has_more = len(rows) > first

        # Remove the extra record used to detect the next page.
        rows = rows[:first]

        users = [
            User(
                id=row[0],
                name=row[1],
                email=row[2],
            )
            for row in rows
        ]

        return users, has_more

    except psycopg.Error as error:
        logger.warning("Using in-memory user pagination: %s", error)

        # Apply the same cursor and limit to the fallback list.
        filtered_users = [
            user for user in memory_data.users
            if user["id"] > (after or 0)
        ]

        has_more = len(filtered_users) > first

        return [
            User(
                id=user["id"],
                name=user["name"],
                email=user["email"],
            )
            for user in filtered_users[:first]
        ], has_more
