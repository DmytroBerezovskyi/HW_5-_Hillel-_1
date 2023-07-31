import json
from . import models


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if "admin" in request.path.split("/"):
            pass
        else:
            models.LogModel(
                request=json.dumps(request.GET) if not request.POST else json.dumps(request.POST),
                path=request.path,
                method=request.method,
                query=dict(request.POST) if request.method == "POST" else " ",
                body=request.body if request.method == "POST" else " ",
            ).save()
            # print(request.META.get('QUERY_STRING', False))
