import graphene
from graphql.error import GraphQLError

from .models import News as NewsModel
from .types import NewsType


class Query(graphene.ObjectType):
    all_news = graphene.List(NewsType)
    news_by_id = graphene.Field(NewsType, id=graphene.String())

    def resolve_all_news(self, info):
        newss_ = NewsModel.objects.all()
        return newss_

    def resolve_news_by_id(root, info, id):

        return NewsModel.objects.get(pk=id)


class AddNews(graphene.Mutation):
    news = graphene.Field(NewsType)

    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)

    def mutate(self, info, title="", body=""):
        if not info.context.user.is_authenticated:
            raise GraphQLError("User not authenticated!")
        news = NewsModel(title=title, body=body, user=info.context.user)
        news.save()
        return AddNews(
            title=title,
            body=body,
        )


class Mutation(graphene.ObjectType):
    add_news = AddNews.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
