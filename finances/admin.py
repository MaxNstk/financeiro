# from django.contrib import admin
#
# from finances.models import Category, Transaction
#
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'description']
#     prepopulated_fields = {'slug': ('name',)}
#
#
# @admin.register(Transaction)
# class TransactionAdmin(admin.ModelAdmin):
#     list_display = ['name','category', 'type',
#                     'value', 'description', 'date']