from django.urls import reverse_lazy
from django.views.generic import DeleteView

from finances.models import Transaction


class TransactionDeleteView(DeleteView):

    model = Transaction
    template_name = 'finances/transaction/transaction_delete.html'
    success_url = reverse_lazy('finances:transaction_list')