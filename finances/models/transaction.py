from django.db import models
from django.db.models.signals import post_save

from account.models.base import BaseModel
from finances.models.wallet import Wallet


class Transaction(BaseModel):

    CREDIT = 1
    EXPENSE = 2

    type_CHOICES = [(CREDIT, 'CREDIT'),
                    (EXPENSE, 'EXPENSE')]

    name = models.CharField(max_length=250)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    wallet = models.ForeignKey('Wallet', on_delete=models.DO_NOTHING)
    type = models.IntegerField(choices=type_CHOICES, default=2)
    value = models.FloatField()
    image = models.ImageField(upload_to='images/transaction/', null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.name


def update_wallet_value(sender, instance, **kwargs):
    wallet = Wallet.objects.get(id=instance.wallet.id)
    if instance.type == Transaction.CREDIT:
        wallet.balance += instance.value
    else:
        wallet.balance -= instance.value
    wallet.save()


post_save.connect(update_wallet_value, sender=Transaction)
