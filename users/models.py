from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=False, default=18)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.username

# class Evento(models.Model):
#     # About Event
#     TYPE_EVENTS = (
#         ('BO', 'Boda'),
#         ('XV', 'XV Años'),
#         ('BA', 'Bautizos'),
#         ('IN', 'Infantiles'),
#         ('PH', 'Para él'),
#         ('PM', 'Para ella')
#     )
#     id = models.BigAutoField(primary_key=True)
#     event_type = models.CharField(max_length=2, choices=TYPE_EVENTS, blank=False)
#     date = models.DateField(blank=False)
#     time = models.TimeField(blank=False)
#     guests = models.TextField(max_length=2000)
    
#     anfitrion = models.ForeignKey(Anfitrion, on_delete=models.CASCADE, null=False, related_name="anfitrion_user_set")
#     festejado = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, related_name="cliente_user_set")

#     def __str__(self):
#         return str(self.event_type)