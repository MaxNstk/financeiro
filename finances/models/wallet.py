from django.db import models

from account.models.base import BaseModel


class Wallet(BaseModel):

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=True, blank=True)
    balance = models.FloatField()

    def __str__(self):
        return self.name