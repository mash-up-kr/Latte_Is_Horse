from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('추가필드', {'fields': ('img_profile',)}),
    ) + BaseUserAdmin.fieldsets
    list_display = (
        'id',
        'username',
        'password',
        'name',
        'type',
        'img_profile',
    )
