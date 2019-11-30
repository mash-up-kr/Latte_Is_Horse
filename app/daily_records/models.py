from django.conf import settings
from django.db import models

from utils.django.models import TimeStampedModel


class DailyRecord(TimeStampedModel):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='daliy_records'
    )
    is_fit = models.BooleanField(null=True, default=True)
    date = models.DateField(null=True)

    def __str__(self):
        return f'Daily Record - {self.date}'
