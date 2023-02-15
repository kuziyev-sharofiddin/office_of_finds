from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager

class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, null=True, blank=True, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=15,null=True, blank=True, unique=True)
    password = models.CharField(max_length=200, null=True, blank=True)


    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()
