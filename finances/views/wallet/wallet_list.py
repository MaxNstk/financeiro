from django.views.generic import ListView

from finances.models import Wallet


class WalletListView(ListView):

    model = Wallet
    template_name = 'finances/wallet/wallet_list.html'