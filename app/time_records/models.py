from django.db import models
from django.conf import settings
from daily_records.models import TimeStampedModel, DailyRecord


class TimeRecord(TimeStampedModel):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='time_records'
    )
    daily_record = models.ForeignKey(
        DailyRecord,
        on_delete=models.CASCADE,
        null=True,
        related_name='time_records'
    )

    def __str__(self):
        return f'Time Record - {self.creator}'
