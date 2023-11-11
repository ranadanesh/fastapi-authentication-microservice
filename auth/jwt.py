import jwt
import datetime
import uuid
from dotenv import dotenv_values


def create_access_token(email):
    jti = uuid.uuid4().hex
    return jwt.encode(
        {
            "email": email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
            "iat": datetime.datetime.utcnow(),
            "jti": jti
        },
        'secret', algorithm="HS256")


def decode_access_token(token):
    payload = jwt.decode(token, 'secret', algorithm='HS256')
    return payload


def create_refresh_token(email):
    jti = uuid.uuid4().hex
    return jwt.encode(
        {
            "email": email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=10),
            "iat": datetime.datetime.utcnow(),
            "jti": jti
        },
        'secret', algorithm="HS256")


def decode_refresh_token(token):
    payload = jwt.decode(token, 'secret', algorithm='HS256')
    return payload
