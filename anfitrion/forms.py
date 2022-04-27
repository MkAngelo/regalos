"""ANFITRION USER"""

from .models import Anfitrion
from django import forms

class AnfitrionForm(forms.ModelForm):
    model = Anfitrion
    fields = (
        'email',
        'first_name',
        'last_name',
        'age',
        'phone_number'
    )

class AnfitrionForm(forms.Form):
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)
    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )
    age = forms.IntegerField()
    phone_number = forms.CharField(max_length=15)