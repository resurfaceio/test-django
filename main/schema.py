import graphene

from .models import Logs
from .mutations import AddLog
from .types import LogsType


class Query(graphene.ObjectType):
    logs = graphene.List(LogsType)

    def resolve_logs(self, ingo):
        logs_ = Logs.objects.all()
        return logs_


class Mutation(graphene.ObjectType):
    add_log = AddLog.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
