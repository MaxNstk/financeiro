from django.views.generic import ListView

from finances.models import Transaction


class TransactionListView(ListView):

    model = Transaction
    template_name = 'finances/transaction/transaction_list.html'
