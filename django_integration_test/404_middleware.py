import json

from django.http import HttpResponse


class JSON404Middleware(object):
    """
    Returns JSON 404 instead of HTML
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if (
            response.status_code == 404
            and "application/json" not in response["content-type"]
        ):
            data = {"detail": "{0} not found".format(request.path)}
            response = HttpResponse(
                json.dumps(data), content_type="application/json", status=404
            )
        return response
