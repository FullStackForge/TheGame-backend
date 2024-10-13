from ninja import Router
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from .schemas import UserSignupSchema, LoginSchema, UserSchema
from jose import jwt
from django.conf import settings
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from ninja.responses import Response

load_dotenv()  # Load environment variables from .env file
SECRET_KEY = os.getenv('SECRET_KEY')

router = Router()
User = get_user_model()

def create_token(user):
    payload = {
        "user_id": user.id,
        "exp": datetime.utcnow() + timedelta(days=1)  # Token expiration
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

@router.post("/signup", response=UserSchema)
def signup(request, user_data: UserSignupSchema):
    user = User.objects.create(
        username=user_data.username,
        email=user_data.email,
        password=make_password(user_data.password)
    )
    return user

@router.post("/login")
def login(request, login_data: LoginSchema):
    print("Login attempt for:", login_data.email)  # Log the login attempt
    user = authenticate(username=login_data.email, password=login_data.password)
    
    if user is not None:
        token = create_token(user)
        return Response(UserSchema(
            id=user.id,
            username=user.username,
            email=user.email,
            token=token
        ).dict())
    print("Authentication failed for:", login_data.email)  # Log failure
    return Response({"error": "Invalid credentials"}, status=401)

@router.get("/me", response=UserSchema)
def get_user(request):
    user = request.auth.user  # Automatically get user from auth token
    return user
