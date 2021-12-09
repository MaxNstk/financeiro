from django.urls import reverse_lazy
from django.views.generic import UpdateView

from finances.forms.wallet.wallet_form import Walletform
from finances.models import Wallet


class WalletUpdateView(UpdateView):

    model = Wallet
    template_name = 'finances/wallet/wallet_form.html'
    form_class = Walletform
    success_url = reverse_lazy('finances:wallet_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super(WalletUpdateView, self).form_valid(form)
        except Exception as e:
            return e
