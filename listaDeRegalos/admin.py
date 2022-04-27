from django.contrib import admin
from .models import ListaDeRegalos

# Register your models here.
class ListaDeRegalosAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'description',
        'store',
        'price',
        'image'
    )
    list_display_links = ('type','store')
    search_fields = (
        'type',
        'store',
        'price'
    )
admin.site.register(ListaDeRegalos, ListaDeRegalosAdmin)