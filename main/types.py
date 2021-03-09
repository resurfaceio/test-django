import graphene
from graphene_django import DjangoObjectType

from .models import News


class NewsType(DjangoObjectType):
    class Meta:
        model = News


class NewsInput(graphene.InputObjectType):
    news = graphene.String()
