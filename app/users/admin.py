from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    filedsets = (
        ('추가필드', {'field': ('img_profile',
                            )}),
    )
    list_display = (
        'id',
        'username',
        'password',
        'name',
        'type',
    )
