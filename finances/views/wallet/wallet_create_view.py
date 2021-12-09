from django.urls import reverse_lazy
from django.views.generic import CreateView

from finances.forms.wallet.wallet_create_form import WalletCreateForm
from finances.models import Wallet


class WalletCreateView(CreateView):

    model = Wallet
    form_class = WalletCreateForm
    template_name = 'finances/wallet/wallet_form.html'
    success_url = reverse_lazy('finances:wallet_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super(WalletCreateView, self).form_valid(form)
        except Exception as e:
            return self.form_invalid(form)