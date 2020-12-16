from sanic_jwt import exceptions
from user import User
import json
import config

username_table = {}
userid_table = {}


def load_valid_users_file():
    global username_table
    global userid_table

    with open(config.valid_users_file) as json_file:
        valid_users_raw = json.load(json_file)

    users = []
    for json_user in valid_users_raw:
        users.append(User(json_user["id"], json_user["name"], json_user["password"]))

    username_table = {u.username: u for u in users}
    userid_table = {u.user_id: u for u in users}


async def authenticate(request, *args, **kwargs):
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    user = username_table.get(username, None)
    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if password != user.password:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return user
