"""CLIENTE ADMIN"""

from django.contrib import admin
from .models import Cliente

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'first_name',
        'last_name',
        'age'
    ]
admin.site.register(Cliente, ClienteAdmin)