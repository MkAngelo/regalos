
from django.db import models
from users.models import CustomUser

class Anfitrion(CustomUser, models.Model):
    phone = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return self.first_name

class Evento(models.Model):
    # About Event
    TYPE_EVENTS = (
        ('BO', 'Boda'),
        ('XV', 'XV Años'),
        ('BA', 'Bautizos'),
        ('IN', 'Infantiles'),
        ('PH', 'Para él'),
        ('PM', 'Para ella')
    )
    id = models.BigAutoField(primary_key=True)
    event_type = models.CharField(max_length=2, choices=TYPE_EVENTS, blank=False)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
    guests = models.TextField(max_length=2000)
    address = models.TextField(max_length=500)
    
    anfitrion = models.ForeignKey(Anfitrion, on_delete=models.CASCADE, null=False, related_name="anfitrion_user_set")
    festejado = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, related_name="cliente_user_set")

    def __str__(self):
        return str(self.event_type)