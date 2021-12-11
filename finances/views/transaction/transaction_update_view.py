from django.urls import reverse_lazy

from finances.forms.transaction.transaction_form import TransactionForm
from finances.models import Transaction
from finances.views.generic.custom_update_view import CustomUpdateView


class TransactionUpdateView(CustomUpdateView):

    model = Transaction
    template_name = 'generic/generic_form.html'
    form_class = TransactionForm
    success_url = reverse_lazy('finances:transaction_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super(TransactionUpdateView, self).form_valid(form)
        except Exception as e:
            return self.form_invalid(form)