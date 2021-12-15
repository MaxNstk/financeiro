from finances.models import Transaction
from finances.views.generic.custom_list_view import CustomListView


class TransactionListView(CustomListView):

    model = Transaction
    template_name = 'finances/transaction/transaction_list.html'
    breadcrumbs = 'Criação de Transação'
