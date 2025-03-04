from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import User

# User Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect after signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form, 'user': request.user})

# User Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirect based on user role
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'patron':
                return redirect('patron_dashboard')
            else:
                return redirect('student_dashboard')
            # return redirect('dashboard')
    return render(request, 'auth/login.html', {'user': request.user})

# User Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard View with Logged-in User Info
@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

@login_required
def patron_dashboard(request):
    return render(request, 'patron_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@login_required(login_url='/login/')  # Redirect to login page if not logged in
def dashboard(request):
    return render(request, 'club_management/dashboard.html')
