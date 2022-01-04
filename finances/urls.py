from django.contrib.auth.decorators import login_required
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
    path('wallet_create', login_required(WalletCreateView.as_view()), name='wallet_create'),
    path('wallet_list', login_required(WalletListView.as_view()), name='wallet_list'),
    path('wallet_update/<int:pk>', login_required(WalletUpdateView.as_view()), name='wallet_update'),
    path('wallet_delete/<int:pk>', login_required(WalletDeleteView.as_view()), name='wallet_delete'),

    path('category_create', login_required(CategoryCreateView.as_view()), name='category_create'),
    path('category_list', login_required(CategoryListView.as_view()), name='category_list'),
    path('category_update/<int:pk>', login_required(CategoryUpdateView.as_view()), name='category_update'),
    path('category_delete/<int:pk>', login_required(CategoryDeleteView.as_view()), name='category_delete'),

    path('transaction_create', login_required(TransactionCreateView.as_view()), name='transaction_create'),
    path('transaction_list', login_required(TransactionListView.as_view()), name='transaction_list'),
    path('transaction_update/<int:pk>', login_required(TransactionUpdateView.as_view()), name='transaction_update'),
    path('transaction_delete/<int:pk>', login_required(TransactionDeleteView.as_view()), name='transaction_delete'),

]
