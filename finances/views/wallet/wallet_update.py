from django.views.generic import UpdateView

from finances.models import Wallet


class WalletUpdateView(UpdateView):

    model = Wallet
    template_name = 'finances/wallet/wallet_form.html'
    fields = '__all__'
