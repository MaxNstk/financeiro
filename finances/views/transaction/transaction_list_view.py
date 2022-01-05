from finances.models import Transaction, Wallet, Category
from finances.views.generic.custom_list_view import CustomListView


class TransactionListView(CustomListView):

    model = Transaction
    template_name = 'finances/transaction/transaction_list.html'
    breadcrumbs = 'Listagem de Transação'

    def get_context_data(self, **kwargs):
        ctx = super(TransactionListView, self).get_context_data()
        if Wallet.objects.filter(user=self.request.user).count() == 0:
            ctx['hasnt_wallet'] = True
        if Category.objects.filter(user=self.request.user).count() == 0:
            ctx['hasnt_category'] = True
        return ctx
