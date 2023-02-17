from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, null=True, blank=True, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = PhoneNumberField()
    password = models.CharField(max_length=200, null=True, blank=True)


    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    # objects = UserManager()
# class CustomUser(AbstractUser):
#     phone_number = PhoneNumberField()
