from django.contrib import admin
from . import models


@admin.register(models.TimeRecord)
class TimeRecordAdmin(admin.ModelAdmin):
    list_display = (
      'id',
      'creator',
      'created_at',
    )


