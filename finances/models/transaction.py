from datetime import datetime

from django.db import models
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from account.models.base import BaseModel
from finances.models.wallet import Wallet


class Transaction(BaseModel):

    CREDIT = 1
    EXPENSE = 2

    type_CHOICES = [(CREDIT, 'Renda'),
                    (EXPENSE, 'Despesa')]

    name = models.CharField(max_length=250)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE)
    type = models.IntegerField(choices=type_CHOICES, default=2)
    value = models.FloatField()
    description = models.TextField(max_length=255, null=True, blank=True)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Transaction)
def update_wallet_balance(instance, **kwargs):

    current_transaction = instance
    wallet = Wallet.objects.get(id=instance.wallet.id)

    # if the transactions is being updated:
    if instance.id:
        old_transaction = Transaction.objects.get(id=current_transaction.id)

        if old_transaction.type == Transaction.CREDIT:
            wallet.balance -= old_transaction.value
        else:
            wallet.balance += old_transaction.value

        # adding or increasing the new value on the wallet based on the type
    if instance.type == Transaction.CREDIT:
        wallet.balance += current_transaction.value
    else:
        wallet.balance -= current_transaction.value
    wallet.save()


@receiver(pre_delete, sender=Transaction)
def update_wallet_balance_on_delete(instance, **kwargs):

    wallet = instance.wallet

    if instance.type == Transaction.CREDIT:
        wallet.balance -= instance.value
    else:
        wallet.balance += instance.value
    wallet.save()