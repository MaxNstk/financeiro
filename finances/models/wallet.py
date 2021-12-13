from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models.base import BaseModel


class Wallet(BaseModel):

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=True, blank=True)
    balance = models.FloatField(default=0)
    initial_balance = models.FloatField(null=True, blank=True)
    main = models.BooleanField(default=False)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Wallet)
def set_initial_balance(instance, created, **kwargs):

    if created:
        instance.initial_balance = instance.balance
        instance.save()