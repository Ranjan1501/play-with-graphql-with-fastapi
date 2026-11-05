import strawberry

@strawberry.type
class Order:
    id: int
    amount: float