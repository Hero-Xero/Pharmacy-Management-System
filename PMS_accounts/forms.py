from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Client

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ClientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['date_of_birth', 'phone_number', 'address', 'is_active']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))
