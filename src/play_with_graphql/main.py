# FastAPI is our Python web framework.
from fastapi import FastAPI

# GraphQLRouter connects a Strawberry GraphQL schema to FastAPI.
from strawberry.fastapi import GraphQLRouter

# Import our GraphQL schema.
from play_with_graphql.graphql.schema import schema


# Create a FastAPI application instance.
#
# app is the object that Uvicorn will use to run our application.
app = FastAPI()


# Create a GraphQL router.
#
# We pass our schema so Strawberry knows which
# queries and mutations are supported.
graphql_app = GraphQLRouter(schema)


# Register the GraphQL router with FastAPI.
#
# prefix="/graphql" means all GraphQL requests
# will be handled through the /graphql URL.
app.include_router(
    graphql_app,
    prefix="/graphql"
)