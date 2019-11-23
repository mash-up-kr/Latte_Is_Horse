from django.db import models
from time_records.models import TimeRecord


class Brand(models.Model):
    name = models.CharField('브랜드이름', max_length=100)
    image = models.ImageField(upload_to='brand', null=True)

    def __str__(self):
        return self.name


class Beverage(models.Model):
    beverage_name = models.CharField('음료이름', max_length=100)
    caffeine = models.IntegerField()
    volume = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    time_record = models.ForeignKey(TimeRecord, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.beverage_name}, {self.caffeine}, {self.volume}, {self.brand}'
