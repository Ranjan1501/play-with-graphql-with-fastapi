# Import the Book class from our models directory.
from play_with_graphql.models.book import Book


# This is our temporary in-memory database.
#
# A Python list stores multiple values.
# Here, we are storing Book objects inside the list.
#
# The data will remain available while the application is running.
# Restarting the application will reset this list.
books = [
    Book(
        id=1,
        title="Atomic Habits",
        author="James Clear"
    ),
    Book(
        id=2,
        title="The Psychology of Money",
        author="Morgan Housel"
    )
]


# Function to fetch all books.
def get_all_books() -> list[Book]:

    # Return the complete list of books.
    #
    # list[Book] is a type hint indicating that
    # this function returns a list containing Book objects.
    return books


# Function to fetch a particular book using its ID.
def get_book_by_id(book_id: int) -> Book | None:

    # Loop through each book in our books list.
    for book in books:

        # Check whether the current book ID matches the requested ID.
        if book.id == book_id:
            return book

    # If no matching book is found, return None.
    #
    # None represents the absence of a value in Python.
    return None


# Function to create a new book.
def create_book(title: str, author: str) -> Book:

    # Find the highest existing ID.
    # max() returns the largest value from a collection.
    #
    # If the list is empty, use 0 as the default.
    highest_id = max(
        (book.id for book in books),
        default=0
    )

    # Generate the next ID.
    new_id = highest_id + 1

    # Create a new Book object.
    new_book = Book(
        id=new_id,
        title=title,
        author=author
    )

    # append() adds an item to the end of a Python list.
    books.append(new_book)

    # Return the newly created book.
    return new_book