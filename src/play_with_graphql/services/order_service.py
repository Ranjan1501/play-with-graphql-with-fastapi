import logging

import psycopg

from play_with_graphql.database.db import execute_query
from play_with_graphql.models.order import Order
from play_with_graphql.services import memory_data

logger = logging.getLogger(__name__)


def get_orders_by_user_id(user_id: int) -> list[Order]:

    try:
        # Fetch orders belonging to one user.
        # This query runs once for every user in our N+1 experiment.
        rows = execute_query(
            """
            SELECT id, amount
            FROM orders
            WHERE user_id = %s
            ORDER BY id
            """,
            (user_id,)
        )

        return [
            Order(id=row[0], amount=float(row[1]))
            for row in rows
        ]

    except psycopg.Error as error:
        logger.warning(
            "Could not fetch orders for user %s from PostgreSQL: %s",
            user_id,
            error
        )

        # Fallback: filter the in-memory order list.
        return [
            Order(id=order["id"], amount=order["amount"])
            for order in memory_data.orders
            if order["user_id"] == user_id
        ]