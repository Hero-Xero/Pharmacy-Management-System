from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinLengthValidator


class User(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('manager', 'Manager'),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    
    def is_client(self):
        return self.role == 'client'

    def is_manager(self):
        return self.role == 'manager'

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        if self.role == 'manager':
            self.is_staff = True  
        super().save(*args, **kwargs)


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            MinLengthValidator(5),  # Minimum length of 5 characters
            RegexValidator(
                regex=r'^\d{5,15}$',
                message="Phone number must be between 5 and 15 digits long and contain only numbers.",
                code="invalid_phone_number"
            )
        ]
    )

    address = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
    city = models.CharField(max_length=50, blank=True, null=True)
    governerate = models.CharField(max_length=50, blank=True, null=True)

    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)


    @property
    def email(self):
        return self.user.email
    
    @property
    def password(self):
        return self.user.password
    
    def __str__(self):
        return f"Username:{self.user}, add:{self.address} date:{self.date_of_birth} phone:{self.phone_number} city:{self.city} gover:{self.governerate} ({self.first_name} {self.last_name}), date_joined:{self.date_joined}, last_login:{self.last_login}"


class Categories(models.Model):
    category = models.CharField(max_length=10, unique=True, blank=False, null=False)
    
    def __str__(self):
        return self.category
    