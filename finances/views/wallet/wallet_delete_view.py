from django.urls import reverse_lazy

from finances.models import Wallet
from finances.views.generic.custom_delete_view import CustomDeleteView


class WalletDeleteView(CustomDeleteView):

    model = Wallet
    success_url = reverse_lazy('finances:wallet_list')
    template_name = 'finances/wallet/wallet_delete.html'