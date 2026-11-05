import strawberry

from play_with_graphql.models.order import Order
from play_with_graphql.services.order_service import get_orders_by_user_id


@strawberry.type
class User:
    id: int
    name: str
    email: str

    # Holds orders fetched by the optimized batch query.
    # Private means it won't be exposed in the GraphQL schema.
    _loaded_orders: strawberry.Private[list[Order] | None] = None

    @strawberry.field
    def orders(self) -> list[Order]:

        # If orders were already fetched in bulk, return them.
        if self._loaded_orders is not None:
            return self._loaded_orders

        # Otherwise, use the original N+1 implementation.
        return get_orders_by_user_id(self.id)