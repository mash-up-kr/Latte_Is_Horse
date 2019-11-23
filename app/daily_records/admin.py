from django.contrib import admin
from . import models


@admin.register(models.DailyRecord)
class DailyRecordAdmin(admin.ModelAdmin):
    list_display = (
      'id',
      'creator',
      'is_fit',
      'date'
    )
