from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, required=True)
    class Meta:
        model = User  # Use our custom User model
        fields = ['username', 'email', 'password1', 'password2', 'role']
