from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinLengthValidator

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True  
    )
    
    phone_number = forms.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\d{5,15}$',
                message="Phone number must be between 5 and 15 digits long and contain only numbers.",
                code="invalid_phone_number"
            )
        ]
    )
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    governerate = forms.CharField(max_length=50)
