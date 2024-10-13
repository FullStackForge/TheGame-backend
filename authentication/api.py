# from ninja import Router
# from django.contrib.auth import get_user_model, authenticate
# from django.contrib.auth.hashers import make_password
# from .schemas import UserSignupSchema, LoginSchema, UserSchema
# from .auth import AuthBearer
# from jose import jwt
# from django.conf import settings
# import datetime
# from .views import create_token
# router = Router()
# User = get_user_model()

# @router.post("/signup", response=UserSchema)
# def signup(request, user_data: UserSignupSchema):
#     user = User.objects.create(
#         username=user_data.username,
#         email=user_data.email,
#         password=make_password(user_data.password)
#     )
#     return user

# @router.post("/login", response={200: LoginSchema, 401: str})
# def login(request, login_data: LoginSchema):
#     user = authenticate(username=login_data.email, password=login_data.password)
#     if user is not None:
#         token = create_token(user)
#         return {200: {"token": token}}  # This is the expected response structure
#     return 401, "Invalid credentials" # Unauthorized error

# @router.get("/me", response=UserSchema, auth=AuthBearer())
# def get_user(request, user_id: int):
#     user = User.objects.get(id=user_id)
#     return user