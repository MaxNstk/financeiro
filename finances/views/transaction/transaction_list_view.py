from django.views.generic.edit import FormMixin

from finances.forms.transaction.transaction_filter_form import TransactionFilterForm
from finances.models import Transaction, Category
from finances.views.generic.custom_list_view import CustomListView
from finances.views.transaction.transaction_filter_view import TransactionFilterView


class TransactionListView(TransactionFilterView, CustomListView, FormMixin):

    model = Transaction
    template_name = 'finances/transaction/transaction_list.html'
    breadcrumbs = 'Listagem de Transação'
    form_class = TransactionFilterForm

    def get_context_data(self, **kwargs):
        ctx = super(TransactionListView, self).get_context_data()
        ctx['filter_form'] = self.form_class
        return ctx

    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.request.user)
        if self.filters:
            queryset = self.filter_date(queryset)
            queryset = self.filter_category(queryset)
            queryset = self.filter_value(queryset)
            queryset = self.filter_type(queryset)
        return queryset