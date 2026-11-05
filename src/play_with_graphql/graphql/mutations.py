
import strawberry

from play_with_graphql.models.book import Book
from play_with_graphql.services.book_service import create_book


# @strawberry.input tells Strawberry that this class
# represents an input object that GraphQL clients can send.
#
# Unlike @strawberry.type, this is specifically designed
# for incoming data.
@strawberry.input
class BookInput:

    # These fields represent the information
    # required to create a new book.
    title: str
    author: str


@strawberry.type
class Mutation:

    @strawberry.mutation
    def add_book(self, book_data: BookInput) -> Book:

        # book_data is an object containing title and author.
        #
        # We access its properties using dot notation.
        # This is similar to accessing properties of an
        # object in JavaScript.
        return create_book(
            title=book_data.title,
            author=book_data.author
        )
