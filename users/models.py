from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(
        ('email address'), 
        unique=True 
    )
    age = models.PositiveIntegerField(null=False, default=18)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name','age','username']

    
