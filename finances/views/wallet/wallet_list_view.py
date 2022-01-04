from finances.models import Wallet
from finances.views.generic.custom_list_view import CustomListView


class WalletListView(CustomListView):

    model = Wallet
    template_name = 'finances/wallet/wallet_list.html'
    breadcrumbs = 'Listagem de Carteira'

