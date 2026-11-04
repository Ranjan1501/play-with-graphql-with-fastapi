# Import Strawberry.
# Strawberry helps us convert Python classes into GraphQL types.
import strawberry


# @strawberry.type is a decorator.
# A decorator adds functionality to an existing Python class or function.
#
# Here, Strawberry converts this Python class into a GraphQL object type.
@strawberry.type
class Book:

    # These are Python type hints.
    # int means integer, str means string.
    id: int
    title: str
    author: str