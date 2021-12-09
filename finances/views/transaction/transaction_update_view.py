from django.urls import reverse_lazy
from django.views.generic import UpdateView

from finances.forms.transaction.transaction_form import TransactionForm
from finances.models import Transaction


class TransactionUpdateView(UpdateView):

    model = Transaction
    template_name = 'finances/transaction/transaction_form.html'
    form_class = TransactionForm
    success_url = reverse_lazy('finances:transaction_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super(TransactionUpdateView, self).form_valid(form)
        except Exception as e:
            return self.form_invalid(form)