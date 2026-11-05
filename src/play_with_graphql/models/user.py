import strawberry
from play_with_graphql.models.order import Order

@strawberry.type
class User:
    id: int
    name: str
    orders: list[Order]