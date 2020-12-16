# login with a correct user:
curl http://localhost:8888/auth_user \
-d '{"username": "user1", "password": "abcxyz"}' \
-iv -H "Content-Type: application/json"