from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from graphene_django.views import GraphQLView


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass


def pong(request):
    return JsonResponse({"msg": "pong"})
