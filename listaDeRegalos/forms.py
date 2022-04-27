from django import forms
from .models import ListaDeRegalos

class ListaDeRegalosForm(forms.ModelForm):
    model = ListaDeRegalos
    fields = (
        'type',
        'description',
        'store',
        'price',
        'image'
    )