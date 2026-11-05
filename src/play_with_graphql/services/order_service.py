
import logging

import psycopg

from play_with_graphql.database.db import execute_query
from play_with_graphql.models.order import Order
from play_with_graphql.services import memory_data

logger = logging.getLogger(__name__)


# Original implementation: one query per user.
def get_orders_by_user_id(user_id: int) -> list[Order]:

    try:
        rows = execute_query(
            """
            SELECT id, amount
            FROM orders
            WHERE user_id = %s
            ORDER BY id
            """,
            (user_id,),
        )

        return [
            Order(id=row[0], amount=float(row[1]))
            for row in rows
        ]

    except psycopg.Error as error:
        logger.warning("Using memory fallback: %s", error)

        return [
            Order(
                id=order["id"],
                amount=order["amount"],
            )
            for order in memory_data.orders
            if order["user_id"] == user_id
        ]


# Optimized implementation: one query for multiple users.
def get_orders_by_user_ids(
    user_ids: list[int],
) -> dict[int, list[Order]]:

    if not user_ids:
        return {}

    orders_by_user = {
        user_id: [] for user_id in user_ids
    }

    try:
        placeholders = ", ".join(["%s"] * len(user_ids))

        sql = f"""
            SELECT id, user_id, amount
            FROM orders
            WHERE user_id IN ({placeholders})
            ORDER BY id
        """

        rows = execute_query(sql, tuple(user_ids))

        for row in rows:
            order = Order(
                id=row[0],
                amount=float(row[2]),
            )

            orders_by_user[row[1]].append(order)

        return orders_by_user

    except psycopg.Error as error:
        logger.warning("Using memory fallback: %s", error)

        for order in memory_data.orders:
            user_id = order["user_id"]

            if user_id in orders_by_user:
                orders_by_user[user_id].append(
                    Order(
                        id=order["id"],
                        amount=order["amount"],
                    )
                )

        return orders_by_user
