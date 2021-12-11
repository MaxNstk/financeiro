from django.urls import reverse_lazy

from finances.forms.wallet.wallet_form import Walletform
from finances.models import Wallet
from finances.views.generic.custom_update_view import CustomUpdateView


class WalletUpdateView(CustomUpdateView):

    model = Wallet
    template_name = 'generic/generic_form.html'
    form_class = Walletform
    success_url = reverse_lazy('finances:wallet_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super(WalletUpdateView, self).form_valid(form)
        except Exception as e:
            return e