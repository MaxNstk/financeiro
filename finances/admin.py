from django.contrib import admin

# Register your models here.
from finances.models import Category, Transaction, Wallet


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['name','category', 'wallet', 'type',
                    'value', 'description', 'image', 'date']


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['description', 'balance']