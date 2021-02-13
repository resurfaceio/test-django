import graphene

from .models import Logs
from .types import LogInput, LogsType


class AddLog(graphene.Mutation):
    class Arguments:
        input = LogInput(required=True)

    log = graphene.Field(LogsType)

    def mutate(self, info, input=None):
        log = Logs(log=input.log)
        log.save()
        return AddLog(log=log)
