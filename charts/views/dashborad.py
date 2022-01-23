import json

from django.views.generic import FormView

from finances.forms.transaction.transaction_category_filter_form import TransactionCategoryFilterForm
from finances.forms.transaction.transaction_filter_form import TransactionFilterForm
from finances.models import Transaction, Category
from finances.views.transaction.transaction_filter_view import TransactionFilterView


class DashboardView(TransactionFilterView, FormView):

    form_class = TransactionFilterForm
    template_name = 'generic/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super(DashboardView, self).get_context_data()
        TransactionCategoryFilterForm.base_fields['cat_category'].queryset = Category.objects.filter(user=self.request.user)
        # todo fazer metodo para trazer a categoria com mais transações
        TransactionCategoryFilterForm.base_fields['cat_category'].initial = Category.objects.get(user=self.request.user, name='Mercado')

        ctx['category_filter_form'] = TransactionCategoryFilterForm
        # get the queryset and filters it
        queryset = Transaction.objects.filter(user=self.request.user)
        if self.filters:
            queryset = self.filter_date(queryset)
            queryset = self.filter_category(queryset)
            queryset = self.filter_value(queryset)
            queryset = self.filter_type(queryset)

        # get the total value from all the transactions in the queryset
        ctx['total_value'] = 0
        for obj in queryset:
            ctx['total_value'] += obj.value

        # get all the categories of the queryset
        categories = []
        for obj in queryset:
            categories.append(obj.category)
        qs_categories = set(categories)

        # takes the queryset and the categories above and returns a list for each category
        # containing the name, the total_value of the transactions of the respective category
        # and the percentage of it
        categories = []
        for category in qs_categories:
            value = 0
            for obj in queryset:
                if category == obj.category:
                    value += obj.value

            categories.append({ 'name': category.name,
                                'value': value,
                                'percentage': round((value/ctx['total_value']*100),2)
                                })

        categories_names = []
        categories_values = []
        categories_percentages = []

        for category in categories:
            for k,v in category.items():
                if k == 'name':
                    categories_names.append(v)
                if k == 'value':
                    categories_values.append(v)
                if k == 'percentage':
                    categories_percentages.append(v)

        ctx['categories'] = categories
        ctx['categories_names'] = json.dumps(categories_names)
        ctx['categories_values'] = json.dumps(categories_values)
        ctx['categories_percentages'] = json.dumps(categories_percentages)
        return ctx