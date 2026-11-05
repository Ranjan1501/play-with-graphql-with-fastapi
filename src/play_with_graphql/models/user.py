
import strawberry

from play_with_graphql.models.order import OrderPage
from play_with_graphql.services.order_service import (
    get_orders_page_by_user_id,
)


@strawberry.type
class User:
    id: int
    name: str
    email: str

    @strawberry.field
    def orders(
        self,
        first: int = 10,
        after: int | None = None,
    ) -> OrderPage:

        # Restrict page size to avoid unnecessarily large responses.
        first = max(1, min(first, 100))

        # Fetch only this user's requested order page.
        return get_orders_page_by_user_id(
            user_id=self.id,
            first=first,
            after=after,
        )

@strawberry.type
class UserPage:
    items: list[User]
    next_cursor: int | None
    has_more: bool