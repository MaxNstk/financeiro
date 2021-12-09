from django.urls import reverse_lazy
from django.views.generic import CreateView

from finances.forms.transaction.transaction_form import TransactionForm
from finances.models import Transaction


class TransactionCreateView(CreateView):
    model = Transaction
    success_url = reverse_lazy('finances:transaction_list')
    form_class = TransactionForm
    template_name = 'finances/transaction/transaction_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super(TransactionCreateView, self).form_valid(form)
        except Exception as e:
            return self.form_invalid(form)