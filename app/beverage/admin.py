from django.contrib import admin
from . import models


@admin.register(models.Beverage)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'beverage_name',
        'caffeine',
        'volume',
        'brand',
    )


@admin.register(models.Brand)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
    )
