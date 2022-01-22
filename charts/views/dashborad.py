import json

from finances.models import Transaction, Category
from finances.views.transaction.transaction_filter_view import TransactionFilterView


class DashboardView(TransactionFilterView):

    def get_context_data(self, **kwargs):
        queryset = Transaction.objects.filter(user=self.request.user)
        if self.filters:
            queryset = self.filter_date(queryset)
            queryset = self.filter_category(queryset)
            queryset = self.filter_value(queryset)
            queryset = self.filter_type(queryset)
        ctx = super(DashboardView, self).get_context_data()

        categories = []
        total_value = 0
        percentage_value = {}

        for obj in queryset:
            total_value += obj.value
            percentage_value[obj.category.name] = 0

        for obj in queryset:
            percentage_value[obj.category.name] += obj.value

        for key, value in percentage_value.items():
            percentage_value[key] = {'percentage':round((value/total_value*100), 2),
                                     'value': value}
            categories.append(key)

        values = [float(v['value']) for k, v in percentage_value.items()]


        ctx['total_value'] = total_value
        ctx['percentage_value'] = percentage_value

        ctx['queryset'] = {
            'categories': json.dumps(categories),
            'values': json.dumps(values),
        }
        return ctx