from play_with_graphql.models.user import User
from play_with_graphql.models.order import Order

# Dummy in-memory data.
# Each User object contains a list of Order objects.
users = [
    User(
        id=1,
        name="Ranjan",
        orders=[
            Order(id=101, amount=1500.0),
            Order(id=102, amount=2500.0),
        ],
    ),
    User(
        id=2,
        name="Rahul",
        orders=[
            Order(id=103, amount=3000.0),
        ],
    ),
]


# Find a user by ID.
# Returns the User object if found; otherwise returns None.
def get_user_by_id(user_id: int) -> User | None:
    for user in users:
        if user.id == user_id:
            return user

    return None