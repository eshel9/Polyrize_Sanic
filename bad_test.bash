# login with a correct user, extracting access token:
TOKEN=$(\
curl http://localhost:8888/auth_user \
-d '{"username": "user1", "password": "wrongpass"}' \
-H "Content-Type: application/json" | \
jq -r '.access_token')

echo -e "\ntoken received:" $TOKEN "\n"

curl http://localhost:8888/normalize \
-vi -H "Authorization: Bearer $TOKEN" \
-H "Content-Type: application/json" \
-d '
[
  {
    "name": "device",
    "strVal": "iPhone",
    "metadata": "not interesting"
  },
  {
    "name": "isAuthorized",
    "boolVal": "false",
    "lastSeen": "not interesting"
  }
]
'