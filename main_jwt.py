from sanic import Sanic
from sanic_jwt import initialize
from authentication import authenticate
from normalization import add_normalization_routes

app = Sanic("Eshel' Sanic App")
initialize(app, authenticate=authenticate, url_prefix='/auth_user')
add_normalization_routes(app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8888)
