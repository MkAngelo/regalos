from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


# class CustomUserAdmin(admin.ModelAdmin):
    # list_display = [
    #     'first_name',
    #     'last_name',
    #     'username',
    #     'age',
    #     'email',
    #     'is_staff',
    #     'is_superuser',
    # ]
# admin.site.register(CustomUser)

