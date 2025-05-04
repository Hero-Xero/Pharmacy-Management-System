# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserLoginForm
from django.urls import reverse


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse("marketplace:home"))  # Already logged in

    form = UserLoginForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect(reverse("marketplace:home"))
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect(reverse("marketplace:home"))  # Already logged in

    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect(reverse("marketplace:home"))
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse("marketplace:home"))
