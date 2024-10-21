from django.db import models
from django.contrib.auth.models import AbstractUser #for custom user and we need to add (AUTH_USER_MODEL =) on sattings.py

# Create your models here.
class User_Model(AbstractUser):
    TYPE = [
        ('admin', 'Admin'),
        ('user', 'User')
    ]
    user_type = models.CharField(choices=TYPE, max_length=50, null=True)