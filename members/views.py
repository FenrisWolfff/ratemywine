from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.success(request, 'Invalid username or password.')
                return redirect('login')
        else:
            return render(request, "authentication/login.html")


def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                messages.success(request, 'Registration successful. Please log in now.')
                return redirect('login')
        else:
            form = RegistrationForm()
        return render(request, "authentication/register_user.html", {'form': form})