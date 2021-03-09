import graphene
from graphql.error import GraphQLError

from .models import News
from .types import NewsType


class Query(graphene.ObjectType):
    newss = graphene.List(NewsType)

    def resolve_newss(self, info):
        news_ = News.objects.all()
        return news_


class AddNews(graphene.Mutation):
    news = graphene.Field(NewsType)

    class Arguments:
        news = graphene.String(required=True)

    def mutate(self, info, news):
        if not info.context.user.is_authenticated:
            raise GraphQLError("User not authenticated!")
        news = News(news=news, user=info.context.user)
        news.save()
        return AddNews(news=news)


class Mutation(graphene.ObjectType):
    add_news = AddNews.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
