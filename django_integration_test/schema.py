import graphene
import graphql_jwt
import main.schema

import django_integration_test.core.schema


class Query(
    django_integration_test.core.schema.Query, main.schema.Query, graphene.ObjectType
):
    pass


class Mutation(
    django_integration_test.core.schema.Mutation,
    main.schema.Mutation,
    graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
