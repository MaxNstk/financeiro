from django.urls import path

from finances.views.category.category_delete_view import CategoryDeleteView
from finances.views.category.category_create_view import CategoryCreateView
from finances.views.category.category_list_view import CategoryListView
from finances.views.category.category_update_view import CategoryUpdateView
from finances.views.transaction.transaction_create_view import TransactionCreateView
from finances.views.transaction.transaction_delete_view import TransactionDeleteView
from finances.views.transaction.transaction_list_view import TransactionListView
from finances.views.transaction.transaction_update_view import TransactionUpdateView
from finances.views.wallet.wallet_create_view import WalletCreateView
from finances.views.wallet.wallet_delete_view import WalletDeleteView
from finances.views.wallet.wallet_list_view import WalletListView
from finances.views.wallet.wallet_update_view import WalletUpdateView

app_name = 'finances'

urlpatterns = [
    path('wallet_create', WalletCreateView.as_view(), name='wallet_create'),
    path('wallet_list', WalletListView.as_view(), name='wallet_list'),
    path('wallet_update/<int:pk>', WalletUpdateView.as_view(), name='wallet_update'),
    path('wallet_delete/<int:pk>', WalletDeleteView.as_view(), name='wallet_delete'),

    path('category_create', CategoryCreateView.as_view(), name='category_create'),
    path('category_list', CategoryListView.as_view(), name='category_list'),
    path('category_update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),

    path('transaction_create', TransactionCreateView.as_view(), name='transaction_create'),
    path('transaction_list', TransactionListView.as_view(), name='transaction_list'),
    path('transaction_update/<int:pk>', TransactionUpdateView.as_view(), name='transaction_update'),
    path('transaction_delete/<int:pk>', TransactionDeleteView.as_view(), name='transaction_delete'),

]
