
import strawberry


@strawberry.type
class Order:
    id: int
    amount: float


# Represents one page of orders.
@strawberry.type
class OrderPage:
    items: list[Order]
    next_cursor: int | None
    has_more: bool
