import graphene
from graphql.error import GraphQLError

from .models import Logs
from .types import LogsType


class Query(graphene.ObjectType):
    logs = graphene.List(LogsType)

    def resolve_logs(self, ingo):
        logs_ = Logs.objects.all()
        return logs_


class AddLog(graphene.Mutation):
    log = graphene.Field(LogsType)

    class Arguments:
        log = graphene.String(required=True)

    def mutate(self, info, log):
        if not info.context.user.is_authenticated:
            raise GraphQLError("User not authenticated!")
        log = Logs(log=log, user=info.context.user)
        log.save()
        return AddLog(log=log)


class Mutation(graphene.ObjectType):
    add_log = AddLog.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
