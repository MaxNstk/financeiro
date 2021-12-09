from django.urls import reverse_lazy
from django.views.generic import DeleteView

from finances.models import Wallet


class WalletDeleteView(DeleteView):

    model = Wallet
    success_url = reverse_lazy('finances:wallet_list')
    template_name = 'finances/wallet/wallet_delete.html'