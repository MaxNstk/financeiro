from django.urls import reverse_lazy

from finances.forms.wallet.wallet_form import Walletform
from finances.models import Wallet
from finances.views.generic.custom_create_view import CustomCreateView


class WalletCreateView(CustomCreateView):

    model = Wallet
    form_class = Walletform
    template_name = 'generic/generic_form.html'
    success_url = reverse_lazy('finances:wallet_list')

    breadcrumbs = 'Criação de Carteira'

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super(WalletCreateView, self).form_valid(form)
        except Exception as e:
            return self.form_invalid(form)