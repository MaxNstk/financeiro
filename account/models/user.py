from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=20)
    description = models.CharField(max_length=255, null=True, blank=True)