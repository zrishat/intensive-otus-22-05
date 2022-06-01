from os import environ as env

token_name = env.get("TOKEN_NAME")
if not token_name:
    token_name = 'testtoken'