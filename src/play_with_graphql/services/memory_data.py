# Generate 100 dummy users.
users = [
    {
        "id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com"
    }
    for user_id in range(1, 101)
]


# Generate two dummy orders per user.
orders = [
    {
        "id": (user_id * 10) + order_number,
        "user_id": user_id,
        "amount": 1000.0 + (order_number * 500)
    }
    for user_id in range(1, 101)
    for order_number in range(1, 3)
]

