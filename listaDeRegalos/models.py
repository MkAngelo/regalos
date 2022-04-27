from django.db import models

# Create your models here.
class ListaDeRegalos(models.Model):
    # About Event
    TYPE_EVENTS = (
        ('BO', 'Boda'),
        ('XV', 'XV Años'),
        ('BA', 'Bautizos'),
        ('IN', 'Infantiles'),
        ('PH', 'Para él'),
        ('PM', 'Para ella')
    )
    type = models.CharField(max_length=2, choices=TYPE_EVENTS, blank=False)
    description = models.TextField(max_length=130)
    store = models.CharField(max_length=50)
    price = models.PositiveIntegerField(null=False, default=0)
    image = models.ImageField(upload_to='products/images',blank=True,null=True)

    def __str__(self):
        return self.type