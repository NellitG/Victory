from django.urls import path
from .views import register, login_view, logout_view, dashboard
from club_management.models import User


urlpatterns = [
    path('', dashboard, name="dashboard"),
    path("register/", register, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
