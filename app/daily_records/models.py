from django.db import models
from django.conf import settings


class TimeStampedModel(models.Model):
    """ Base Model """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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
