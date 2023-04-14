from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""
