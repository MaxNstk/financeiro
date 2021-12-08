from django.urls import path

from finances.views.category.category_create_view import CategoryCreateView
from finances.views.category.category_list import CategoryListView
from finances.views.category.category_update import CategoryUpdateView
from finances.views.transaction.transaction_create_view import TransactionCreateView
from finances.views.transaction.transaction_list import TransactionListView
from finances.views.transaction.transaction_update import TransactionUpdateView
from finances.views.wallet.wallet_create import WalletCreateView
from finances.views.wallet.wallet_list import WalletListView
from finances.views.wallet.wallet_update import WalletUpdateView

app_name = 'finances'

urlpatterns = [
    path('wallet_create', WalletCreateView.as_view(), name='wallet_create'),
    path('wallet_list', WalletListView.as_view(), name='wallet_list'),
    path('wallet_update/<int:pk>', WalletUpdateView.as_view(), name='wallet_update'),

    path('category_create', CategoryCreateView.as_view(), name='category_create'),
    path('category_list', CategoryListView.as_view(), name='category_list'),
    path('category_update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),

    path('transaction_create', TransactionCreateView.as_view(), name='transaction_create'),
    path('transaction_list', TransactionListView.as_view(), name='transaction_list'),
    path('transaction_update/<int:pk>', TransactionUpdateView.as_view(), name='transaction_update'),

]
