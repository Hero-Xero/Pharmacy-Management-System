from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import * 
from .forms import RegistrationForm

def index(request):
    return render(request, 'pharma/index.html', {'categories': Categories.objects.all()})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'hi/index.html')
        else:
            return render(request, 'pharma/login.html', {'error': 'Invalid username or password'})
    return render(request, 'pharma/login.html')

def client_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = None
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'].lower(),
                    email=form.cleaned_data['email'].lower(),
                    password=form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name']
                    
                )
                user.role = 'client'
                user.save()

                Client.objects.create(
                    user=user, 
                    date_of_birth=form.cleaned_data['date_of_birth'],
                    phone_number=form.cleaned_data['phone_number'],
                    address=form.cleaned_data['address'],
                    city=form.cleaned_data['city'],
                    governerate=form.cleaned_data['governerate']
                )

                return redirect('users')

            except IntegrityError:
                if user:
                    user.delete()
                return render(request, 'pharma/index.html', {
                    "form": form,
                    "error": "Username or email already exists. Please try again."
                })
        return render(request, 'pharma/register.html', {"form": form})  

    return render(request, 'pharma/register.html', {"form": RegistrationForm()})



def users(request):
    return render(request, 'pharma/users.html', {
        'clients': Client.objects.all(),
    })
    
    
def category(request, category_name):
    category = Categories.objects.get(category=category_name)
    return render(request, 'pharma/category.html', {
        'category': category,
        'products': Product.objects.filter(category=category)
    })