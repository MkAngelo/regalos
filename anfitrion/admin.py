from django.contrib import admin
from .models import Anfitrion, Evento


class AnfitrionAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'first_name',
        'last_name',
        'age',
        'email',
        'phone'
    ]
admin.site.register(Anfitrion, AnfitrionAdmin)

class EventoAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'date', #FALTA EL LUGAR
        'time',
        'anfitrion',
        'festejado'
    ]
admin.site.register(Evento, EventoAdmin)
