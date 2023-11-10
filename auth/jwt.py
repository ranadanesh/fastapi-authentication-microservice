import jwt
import datetime
import uuid
from dotenv import dotenv_values


def create_access_token(username):
    jti = uuid.uuid4().hex
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
            "iat": datetime.datetime.utcnow(),
            "jti": jti
        },
        key=None, algorithm="HS256")


def decode_access_token(token):
    payload = jwt.decode(token, 'secret', algorithm='HS256')
    return payload


def create_refresh_token(username):
    jti = uuid.uuid4().hex
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=10),
            "iat": datetime.datetime.utcnow(),
            "jti": jti
        },
        key=None, algorithm="HS256")


def decode_refresh_token(token):
    payload = jwt.decode(token, 'secret', algorithm='HS256')
    return payload
