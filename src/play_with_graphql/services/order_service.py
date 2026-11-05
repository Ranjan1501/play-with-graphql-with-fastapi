import logging
import psycopg

from play_with_graphql.database.db import execute_query
from play_with_graphql.models.order import Order, OrderPage
from play_with_graphql.services import memory_data

def get_orders_page_by_user_id(
    user_id: int,
    first: int,
    after: int | None = None,
) -> OrderPage:

    cursor_id = after if after is not None else 0

    try:
        # Fetch one extra order to check whether another page exists.
        rows = execute_query(
            """
            SELECT id, amount
            FROM orders
            WHERE user_id = %s
              AND id > %s
            ORDER BY id
            LIMIT %s
            """,
            (user_id, cursor_id, first + 1),
        )

        has_more = len(rows) > first

        rows = rows[:first]

        orders = [
            Order(
                id=row[0],
                amount=float(row[1]),
            )
            for row in rows
        ]

        # The next cursor is the ID of the last returned order.
        next_cursor = orders[-1].id if has_more and orders else None

        return OrderPage(
            items=orders,
            next_cursor=next_cursor,
            has_more=has_more,
        )

    except psycopg.Error as error:
        logger.warning(
            "Using in-memory order pagination for user %s: %s",
            user_id,
            error,
        )

        filtered_orders = [
            order for order in memory_data.orders
            if order["user_id"] == user_id
            and order["id"] > cursor_id
        ]

        has_more = len(filtered_orders) > first

        selected_orders = filtered_orders[:first]

        orders = [
            Order(
                id=order["id"],
                amount=order["amount"],
            )
            for order in selected_orders
        ]

        next_cursor = orders[-1].id if has_more and orders else None

        return OrderPage(
            items=orders,
            next_cursor=next_cursor,
            has_more=has_more,
        )
