"""CLIENTE"""

from users.models import CustomUser
from django import forms

class ClienteForm(forms.ModelForm):
    model = CustomUser
    fields = (
        'first_name',
        'last_name',
        'age'
    )