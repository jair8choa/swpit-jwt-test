import datetime
import jwt

def token_generator(user_id, private_key):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=10),
            'sub': user_id
        }
        return jwt.encode(payload, private_key, algorithm='HS256')

    except Exception as e:
        return e

def token_validator(token, private_key):
    try:
        payload = jwt.decode(token, key=private_key,algorithms=['HS256'])
        return True
    except Exception as e:
        return False

def get_payload(token, private_key):
    try:
        payload = jwt.decode(token, key=private_key, algorithms=['HS256'])
        return payload
    except Exception as e:
        return e