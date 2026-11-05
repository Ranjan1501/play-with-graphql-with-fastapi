import strawberry

from play_with_graphql.models.order import Order
from play_with_graphql.services.order_service import get_orders_by_user_id


@strawberry.type
class User:
    id: int
    name: str
    email: str

    @strawberry.field
    def orders(self) -> list[Order]:

        # This resolver runs when GraphQL requests the user's orders.
        # Each call currently makes a separate database query.
        return get_orders_by_user_id(self.id)