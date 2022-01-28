from django.urls import reverse_lazy

from finances.forms.transaction.transaction_form import TransactionForm
from finances.models import Transaction, Category
from finances.views.generic.custom_create_view import CustomCreateView


class TransactionCreateView(CustomCreateView):

    model = Transaction
    success_url = reverse_lazy('finances:transaction_list')
    form_class = TransactionForm
    template_name = 'generic/generic_form.html'
    breadcrumbs = 'Criação de Transação'

    def get_form_kwargs(self):
        kwargs = super(TransactionCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        if not form.instance.category:
            form.instance.category = Category.objects.get(name='Descategorizado')
        try:
            return super(TransactionCreateView, self).form_valid(form)
        except Exception as e:
            return self.form_invalid(form)
