from django.contrib.auth import authenticate
from ninja.security import HttpBearer
from jose import jwt, JWTError
from django.conf import settings

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get("user_id")
            if user_id:
                return user_id
        except JWTError:
            pass
        return None