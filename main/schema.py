import graphene

from .models import Logs
from .mutations import AddLog
from .types import LogsType


class Query(graphene.ObjectType):
    logs = graphene.List(LogsType)

    def resolve_logs(self, ingo, root):
        logs_ = Logs.objects.all()
        return logs_


class Mutation(graphene.Mutation):
    add_log = graphene.Field(AddLog)


schema = graphene.Schema(query=Query, mutation=Mutation)
