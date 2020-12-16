from sanic.views import HTTPMethodView
from sanic.response import json
from sanic_jwt import protected
from json import loads
import config


class NormalizationView(HTTPMethodView):
    decorators = [protected()]

    def post(self, request):
        body_json = request.body.decode('utf-8')
        body_decoded = loads(body_json)
        normalized = {current["name"]: current[[x for x in current.keys() if "val" in x.lower()][0]] for current in body_decoded}
        return json(normalized)


def add_normalization_routes(app):
    app.add_route(NormalizationView.as_view(), config.normalize_url)
