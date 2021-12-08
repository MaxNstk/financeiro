from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from account.models.base import BaseModel


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


@receiver(pre_save, sender=Transaction)
def update_wallet_balance(instance, **kwargs):

    new_transaction = instance
    wallet = instance.wallet

    "if the transactions is being updated:"
    try:
        " Takes the old transaction and the wallet that is being updated "
        old_transaction = Transaction.objects.get(id=new_transaction.id)

        " if the old type is credit the value is decreased from the wallet, if expense, it's increased "
        if old_transaction.type == Transaction.CREDIT:
            wallet.balance -= old_transaction.value
        else:
            wallet.balance += old_transaction.value
    except:
        pass

        " adding or increasing the new value on the wallet based on the type"
    if instance.type == Transaction.CREDIT:
        wallet.balance += new_transaction.value
    else:
        wallet.balance -= new_transaction.value

    wallet.save()