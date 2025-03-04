from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Club, Membership

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, required=True, label="Select Role")
    class Meta:
        model = User  # Use our custom User model
        fields = ['username', 'email', 'password1', 'password2', 'role']

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'registration_fee']

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['student', 'club', 'role']