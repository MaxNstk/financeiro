from django.views.generic import CreateView

from finances.forms.transaction.transaction_create_form import TransactionCreateForm
from finances.models import Transaction


class TransactionCreateView(CreateView):
    model = Transaction
    success_url = '/'
    form_class = TransactionCreateForm
    template_name = 'finances/transaction/transaction_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super(TransactionCreateView, self).form_valid(form)
        except Exception as e:
            return self.form_invalid(form)