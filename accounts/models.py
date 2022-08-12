from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser): # user -> customuser : setting -> auth user model
    age = models.PositiveIntegerField(null=True, blank=True)   # CharField(null=False, blank=True) 

