from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    recommend_type = (
        ("most_sensitive", "300"),
        ("sensitive", "500"),
        ("least_sensitive", "700"),
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=recommend_type, default="most_sensitive")
