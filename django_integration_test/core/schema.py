import graphene

from .models import User
from .mutations import CreateUser
from .types import UserType


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        users = User.objects.all()
        return users


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
