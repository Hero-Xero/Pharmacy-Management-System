from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def is_client(self):
        return not self.is_staff

    def is_admin(self):
        return self.is_staff

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            MinLengthValidator(5),  
            RegexValidator(
                regex=r'^\d{5,15}$',
                message="Phone number must be between 5 and 15 digits long and contain only numbers.",
                code="invalid_phone_number"
            )
        ]
    )

    address = models.CharField(max_length=100, validators=[MinLengthValidator(10)])

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
        return f"Client {self.user.username}, Address: {self.address}, Date of Birth: {self.date_of_birth}"


