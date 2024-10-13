from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from authentication.views import router as auth_router
from quiz.api import router as quiz_router

api = NinjaAPI()
api.add_router("/questions/", quiz_router)  # Quiz router
api.add_router("/auth/", auth_router)  # Authentication router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
