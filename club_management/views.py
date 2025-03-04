from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect after signup
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form, 'user': request.user})

# User Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html', {'user': request.user})

# User Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard View with Logged-in User Info
@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})
