# Import Strawberry.
import strawberry

# Import our Book type.
from play_with_graphql.models.book import Book

# Import the service function responsible for creating books.
from play_with_graphql.services.book_service import create_book


# Mutation is another special GraphQL root type.
# It defines operations that modify data.
@strawberry.type
class Mutation:

    # @strawberry.mutation exposes this method
    # as a GraphQL mutation operation.
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:

        # Call the service layer to create the book.
        #
        # The service handles object creation and storing the book.
        return create_book(
            title=title,
            author=author
        )