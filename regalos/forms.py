# Django
from django import forms

class MetodoDePagoForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    card = forms.CharField(min_length=19, max_length=19, required=True)
    cvv = forms.CharField(min_length=3, max_length=3, required=True)