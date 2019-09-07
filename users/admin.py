# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm 
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    '''
    Extend the existing UserAdmin class to use our 
    new CustomUser model and our two new forms.
    '''
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'username', 'profile_pic']
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)