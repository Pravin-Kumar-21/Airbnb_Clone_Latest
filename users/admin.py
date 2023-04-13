from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass
