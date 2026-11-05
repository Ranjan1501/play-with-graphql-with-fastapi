import strawberry

from play_with_graphql.models.book import Book
from play_with_graphql.models.user import User

from play_with_graphql.services.book_service import (
    get_all_books,
    get_book_by_id,
)

from play_with_graphql.services.user_service import get_all_users

from play_with_graphql.database.db import (
    reset_query_count,
    get_query_count,
)


@strawberry.type
class Query:

    @strawberry.field
    def hello(self) -> str:
        return "Hello GraphQL!"

    @strawberry.field
    def books(self) -> list[Book]:
        return get_all_books()

    @strawberry.field
    def book(self, book_id: int) -> Book | None:
        return get_book_by_id(book_id)

    @strawberry.field
    def users(self) -> list[User]:

        # Reset our counter before starting the experiment.
        reset_query_count()

        return get_all_users()

    @strawberry.field
    def database_query_count(self) -> int:

        # Read the number of SQL queries executed so far.
        return get_query_count()