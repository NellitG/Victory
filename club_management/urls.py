from django.urls import path
from .views import register, login_view, logout_view
from club_management.models import User


urlpatterns = [
    path("register/", register, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
