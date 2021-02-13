import graphene
import graphql_jwt

import django_integration_test.core.schema

# import main.schema


class Query(django_integration_test.core.schema.Query, graphene.ObjectType):
    pass


class Mutation(
    django_integration_test.core.schema.Mutation,
    graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
# schema = graphene.Schema(query=Query)
