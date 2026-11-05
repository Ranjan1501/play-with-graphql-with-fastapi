import strawberry

from play_with_graphql.models.book import Book
from play_with_graphql.models.user import User, UserPage

from play_with_graphql.services.book_service import (
    get_all_books,
    get_book_by_id,
)

from play_with_graphql.services.user_service import get_users_page

from play_with_graphql.database.db import (
    reset_query_count,
    get_query_count,
)

@strawberry.type
class Query:
    @strawberry.field
    def users(
        self,
        first: int = 20,
        after: int | None = None,
    ) -> UserPage:

        # Restrict the maximum page size.
        first = max(1, min(first, 100))

        reset_query_count()

        # Fetch only the requested user page.
        users, has_more = get_users_page(
            first=first,
            after=after,
        )

        # Return the page and cursor information.
        next_cursor = users[-1].id if has_more and users else None

        return UserPage(
            items=users,
            next_cursor=next_cursor,
            has_more=has_more,
        )

    @strawberry.field
    def database_query_count(self) -> int:
        return get_query_count()