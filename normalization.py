from sanic.views import HTTPMethodView
from sanic.response import text
from sanic.response import json


class NormalizationView(HTTPMethodView):
    def get(self, request):
        return json({"hello": "world"})

    def post(self, request):
        return text('I am post method')


def add_normalization_routes(app):
    app.add_route(NormalizationView.as_view(), '/normalize')
