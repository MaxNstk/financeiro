from django.urls import reverse_lazy

from finances.models import Transaction
from finances.views.generic.custom_delete_view import CustomDeleteView


class TransactionDeleteView(CustomDeleteView):

    model = Transaction
    template_name = 'finances/transaction/transaction_delete.html'
    success_url = reverse_lazy('finances:transaction_list')