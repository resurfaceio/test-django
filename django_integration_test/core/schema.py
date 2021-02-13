import graphene
from graphql import GraphQLError

from .models import User
from .mutations import CreateUser
from .types import UserType


class Query(graphene.ObjectType):
    user = graphene.Field(UserType)

    def resolve_user(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("You are not logged in")
        return user


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
