from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from account.models.base import BaseModel
from finances.models.wallet import Wallet


class Transaction(BaseModel):

    CREDIT = 1
    EXPENSE = 2

    type_CHOICES = [(CREDIT, 'Renda'),
                    (EXPENSE, 'Despesa')]

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

@receiver(post_save, sender=Transaction)
def create_transaction(instance, created, **kwargs):

    if created:
        wallet = Wallet.objects.get(id=instance.wallet.id)
        if instance.type == Transaction.CREDIT:
            wallet.balance += instance.value
        else:
            wallet.balance -= instance.value
        wallet.save()


@receiver(pre_save, sender=Transaction)
def update_transaction(instance, **kwargs):

    try:
        transaction = Transaction.objects.get(instance.id)
        wallet = Wallet.objects.get(id=instance.wallet.id)
        if transaction.type == Transaction.CREDIT:
            wallet.balance -= transaction.value
        else:
            transaction.balance += transaction.value
        wallet.save()
    except:
        pass