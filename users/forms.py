"""USER"""

import email
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','age','username','email')
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','age','username','email')

# class AnfitrionForm(forms.Form):
#     first_name = forms.CharField(min_length=2, max_length=50)
#     last_name = forms.CharField(min_length=2, max_length=50)
#     email = forms.CharField(
#         min_length=6,
#         max_length=70,
#         widget=forms.EmailInput()
#     )
#     age = forms.IntegerField()
#     phone_number = forms.CharField(max_length=15)
