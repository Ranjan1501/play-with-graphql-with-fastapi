# Import Strawberry to define GraphQL types and fields.
import strawberry

# Import our Book type.
from play_with_graphql.models.book import Book
from play_with_graphql.models.user import User

# Import functions from our service layer.
from play_with_graphql.services.book_service import (
    get_all_books,
    get_book_by_id
)

from play_with_graphql.services.user_service import get_user_by_id



# @strawberry.type tells Strawberry that this is a GraphQL type.
#
# Query is a special GraphQL root type.
# It defines which read operations clients can execute.
@strawberry.type
class Query:

    # @strawberry.field exposes this method as a GraphQL field.
    @strawberry.field
    def hello(self) -> str:

        # Return a simple string.
        return "Hello GraphQL!"

    # Resolver to fetch all books.
    @strawberry.field
    def books(self) -> list[Book]:

        # Call our service function.
        # The service handles the actual data retrieval.
        return get_all_books()

    # Resolver to fetch a particular book.
    #
    # book_id is an argument supplied by the GraphQL client.
    # -> Book | None means we can return a Book or None.
    @strawberry.field
    def book(self, book_id: int) -> Book | None:

        # Pass the requested ID to the service layer.
        return get_book_by_id(book_id)


     # New resolver for fetching a user and their orders.
    @strawberry.field
    def user(self, user_id: int) -> User | None:
        return get_user_by_id(user_id)