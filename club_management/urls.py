from django.urls import path
from .views import register, login_view, logout_view, dashboard, patron_dashboard, student_dashboard
from club_management.models import User
from .views import (
    club_list,
    club_create,
    club_update,
    club_delete,
    membership_list,
    membership_create,
    membership_delete
)


urlpatterns = [
    path('', dashboard, name="dashboard"),
    path("register/", register, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("admin_dashboard/", dashboard, name="admin_dashboard"),
    path("patron_dashboard/", dashboard, name="patron_dashboard"),
    path("student_dashboard/", dashboard, name="student_dashboard"),
    
    #Clubs
    path('clubs/', club_list, name='club_list'),
    path('clubs/create/', club_create, name='club_create'),
    path('clubs/update/<int:pk>/', club_update, name='club_update'),
    path('clubs/delete/<int:pk>/', club_delete, name='club_delete'),

    # Memberships
    path('memberships/', membership_list, name='membership_list'),
    path('memberships/create/', membership_create, name='membership_create'),
    path('memberships/delete/<int:pk>/', membership_delete, name='membership_delete'),

]
