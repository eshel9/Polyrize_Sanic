from sanic import Sanic
from sanic_jwt import initialize
from authentication import authenticate, load_valid_users_file
from normalization import add_normalization_routes
import config

app = Sanic(config.app_name)
initialize(app, authenticate=authenticate, url_prefix=config.auth_url)
add_normalization_routes(app)

if __name__ == "__main__":
    load_valid_users_file()
    app.run(host=config.host, port=config.port)
