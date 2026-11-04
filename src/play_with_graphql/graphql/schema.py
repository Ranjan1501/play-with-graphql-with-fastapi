# Import Strawberry.
import strawberry

# Import our Query class.
from play_with_graphql.graphql.queries import Query

# Import our Mutation class.
from play_with_graphql.graphql.mutations import Mutation


# Create the GraphQL schema.
#
# Schema is the central contract of our GraphQL API.
# It tells Strawberry which queries and mutations are available.
schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)