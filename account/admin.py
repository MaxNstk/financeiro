from django.contrib import admin

# Register your models here.
from account.models import User


@admin.register(User)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['username','email', 'phone',]