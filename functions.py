import jwt
import datetime
from fastapi import HTTPException
SECRET_KEY = "pbCI6ImhhbW1hZEBzb2Z0bWF0aWNzLmNvbSJ9LCJleHAiOjE3Mjk0NTA4"
ALGORITHM = "HS256"
EXPIRE_IN_HOURS = 4


def generate_token():
    expiry_time = datetime.datetime.now() + datetime.timedelta(hours=EXPIRE_IN_HOURS)
    user_info = {
        "username": "Hammad Ahmed",
        "user_id": 1,
        "email": "hammad@softmatics.com"
    }
    payload = {
        'sub': user_info,
        'exp': expiry_time
    }
    token = jwt.encode(
        payload=payload,
        key=SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token


def decode_token(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token.get('sub')
    except:
        return None


def is_logged_in(token:str):
    decoded_token = decode_token(token)
    if decoded_token is None:
        raise HTTPException(status_code=401,detail="Invalid token")
    return decoded_token

