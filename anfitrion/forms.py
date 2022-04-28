"""ANFITRION USER"""

from .models import Anfitrion
from django import forms

class AnfitrionForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    
    first_name = forms.CharField(min_length=2,max_length=50)
    last_name = forms.CharField(min_length=2,max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    age = forms.IntegerField()
    phone = forms.CharField(max_length=15)

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = Anfitrion.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('El username ya existe, elija otro')
            #return "El username ya existe, elije otro."
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()
        
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
            #return "Los passwords no coinciden, revisalos."
        
        return data

    def save(self):
        """Create Anfitrion User."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        anfitrion = Anfitrion.objects.update_or_create(**data)