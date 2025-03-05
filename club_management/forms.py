from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Club, Membership

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES, 
        required=True, 
        label="Select Role",
        widget=forms.Select(attrs={
            "class": "w-full p-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-400"
        })
    )

    class Meta:
        model = User  # Use our custom User model
        fields = ['username', 'email', 'password1', 'password2', 'role']
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "w-full p-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-400"
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full p-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-400"
            }),
            "password1": forms.PasswordInput(attrs={
                "class": "w-full p-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-400"
            }),
            "password2": forms.PasswordInput(attrs={
                "class": "w-full p-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-400"
            }),
        }

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'registration_fee']
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full p-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-400"
            }),
            "registration_fee": forms.NumberInput(attrs={
                "class": "w-full p-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-400"
            }),
        }

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['student', 'club', 'role']
        widgets = {
            "student": forms.Select(attrs={
                "class": "w-full p-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-400"
            }),
            "club": forms.Select(attrs={
                "class": "w-full p-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-400"
            }),
            "role": forms.Select(attrs={
                "class": "w-full p-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-400"
            }),
        }
