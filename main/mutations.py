import graphene

from .models import Logs
from .types import LogInput, LogsType


class AddLog(graphene.Mutation):
    log = graphene.Field(LogsType)

    class Arguments:
        log = graphene.String(required=True)

    def mutate(self, info, log):
        log = Logs(log=log)
        log.save()
        return AddLog(log=log)
