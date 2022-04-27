from django.db import models
from users.models import CustomUser

class Cliente(CustomUser):
    def __str__(self):
        return self.first_name