import json

from django.views.generic import FormView

from finances.forms.transaction.transaction_filter_form import TransactionFilterForm
from finances.models import Transaction, Category
from finances.views.transaction.transaction_filter_view import TransactionFilterView


class DashboardView(TransactionFilterView):

    def get_context_data(self, **kwargs):
        queryset = Transaction.objects.filter(user=self.request.user)
        if self.filters:
            queryset = self.filter_date(queryset)
            queryset = self.filter_category(queryset)
            queryset = self.filter_value(queryset)
        ctx = super(DashboardView, self).get_context_data()

        names = [obj.name for obj in queryset]
        categories = []
        for obj in queryset:
            if obj.category:
                categories.append({obj.category.name : obj.category.color})
            else:
                uncategorized = Category.objects.get(name='uncategorized')
                categories.append({uncategorized.name: uncategorized.color})

        types = [int(obj.type) for obj in queryset]
        values = [float(obj.value) for obj in queryset]
        date = [obj.date for obj in queryset]

        ctx['breadcrumbs'] = 'DashboardView'
        ctx['queryset'] = {
            'names': json.dumps(names),
            'categories': json.dumps(categories),
            'types': json.dumps(types),
            'values': json.dumps(values),
            # 'dates': json.dumps(date),
        }
        return ctx