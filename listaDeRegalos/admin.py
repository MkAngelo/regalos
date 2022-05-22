from django.contrib import admin
from .models import ListaDeRegalos

# Register your models here.
class ListaDeRegalosAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'type',
        'description',
        'store',
        'price',
        'image'
    )
    list_display_links = ('type','store')
    search_fields = (
        'pk',
        'type',
    )
admin.site.register(ListaDeRegalos, ListaDeRegalosAdmin)