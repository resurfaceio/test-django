import graphene
from graphene_django import DjangoObjectType

from .models import Logs


class LogsType(DjangoObjectType):
    class Meta:
        model = Logs


class LogInput(graphene.InputObjectType):
    log = graphene.String()
