from django.db import models
from django.contrib import auth

# Create your models here.

# This is the user model(using built-in models of django)
class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return f"@{self.username}"

