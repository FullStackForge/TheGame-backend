# authentication/schemas.py
from ninja import Schema

class UserSignupSchema(Schema):
    username: str
    email: str
    password: str

class LoginSchema(Schema):
    email: str
    password: str

class UserSchema(Schema):
    id: int
    username: str
    email: str
    token: str
