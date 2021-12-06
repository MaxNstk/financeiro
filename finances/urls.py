from django.urls import path

from finances.views.category.category_create_view import CategoryCreateView
from finances.views.transaction.transaction_create_view import TransactionCreateView
from finances.views.transaction.transaction_list import TransactionListView
from finances.views.wallet.wallet_create import WalletCreateView
from finances.views.wallet.wallet_list import WalletListView

app_name = 'finances'

urlpatterns = [
    path('wallet_create', WalletCreateView.as_view(), name='wallet_create'),
    path('wallet_list', WalletListView.as_view(), name='wallet_list'),
    path('category_create', CategoryCreateView.as_view(), name='category_create'),
    path('transaction_create', TransactionCreateView.as_view(), name='transaction_create'),
    path('transaction_list', TransactionListView.as_view(), name='transaction_list'),
]