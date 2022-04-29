from django.contrib import admin
from .models import Anfitrion, Evento
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class AnfitrionAdmin(UserAdmin):
    list_display = [
        'pk',
        'first_name',
        'last_name',
        'age',
        'email',
        'phone',
        'is_staff',
        'is_superuser'
    ]
    list_editable = ('phone',)
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'phone'
    )
    fieldsets = (
        ('Anfitrion',{
            'fields': (
                ('first_name', 'last_name', 'age'),
                ('email', 'phone')
            ),
        }),
    )
#admin.site.register(Anfitrion, AnfitrionAdmin)

class EventoAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'event_type',
        'anfitrion',
        'date', #FALTA EL LUGAR
        'time',
        'address',
        'festejado_first_name',
        'festejado_last_name',
        'festejado_age'
    ]
    list_display_links = ('pk','event_type')
    list_editable = ('festejado_first_name',"festejado_last_name",'festejado_age')
    search_fields = (
        'anfitrion__email',
        'anfitrion__first_name',
        'anfitrion__last_name',
        'anfitrion__phone',
        'event_type',
        'date'
    )

admin.site.register(Evento, EventoAdmin)
# admin.site.unregister(User)
admin.site.register(Anfitrion, AnfitrionAdmin)