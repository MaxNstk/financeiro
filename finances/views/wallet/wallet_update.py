from django.views.generic import UpdateView

from finances.models import Wallet


class WalletUpdateView(UpdateView):

    model = Wallet
    template_name = 'finances/wallet/wallet_form.html'
    exclude = ['user']

    def form_valid(self, form):
        form.instance.user = self.request.user.instance
        try:
            return super(WalletUpdateView, self).form_valid(form)
        except Exception as e:
            return e
