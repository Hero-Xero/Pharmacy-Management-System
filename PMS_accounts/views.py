from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ClientRegistrationForm
from .models import Client, User
from django.db import transaction


def register_client(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        client_form = ClientRegistrationForm(request.POST)

        # Ensure both forms are valid
        if user_form.is_valid() and client_form.is_valid():
            try:
                # Start a database transaction to ensure atomicity
                with transaction.atomic():
                    # Save the User form first, but don't commit it yet
                    user = user_form.save(commit=False)
                    user.save()

                    # Save the Client form and link it to the created User
                    client = client_form.save(commit=False)
                    client.user = user
                    client.save()

                    # After both are saved, log the user in
                    login(request, user)

                    messages.success(request, "Your account has been created successfully!")
                    return redirect('client_dashboard')  # Redirect to the client dashboard or home page

            except Exception as e:
                # If an error occurs, rollback the transaction and show an error
                transaction.rollback()
                messages.error(request, f"Error creating account: {str(e)}")
        else:
            messages.error(request, "Please correct the errors below.")

    else:
        user_form = UserRegistrationForm()
        client_form = ClientRegistrationForm()

    return render(request, 'accounts/register.html', {'user_form': user_form, 'client_form': client_form})



def login_client(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None and not user.is_staff:
            login(request, user)
            return redirect('client_dashboard')
        else:
            messages.error(request, "Invalid credentials or not a client.")
    return render(request, 'accounts/login.html')


@login_required
def logout_client(request):
    logout(request)
    return redirect('login_client')
