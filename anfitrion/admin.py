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

admin.site.register(Evento)
