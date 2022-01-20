import json

from django.views.generic import FormView

from finances.forms.transaction.transaction_filter_form import TransactionFilterForm
from finances.models import Transaction, Category


class DashboardView(FormView):

    form_class = TransactionFilterForm
    template_name = 'generic/dashboard.html'
    filters = {}

    def get_form_kwargs(self):
        kwargs = super(DashboardView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get(self, request, *args, **kwargs):
        self.filters = dict(map(lambda k: (k, request.GET[k]), request.GET))
        if 'csrfmiddlewaretoken' in self.filters:
            self.filters.pop('csrfmiddlewaretoken')
        return super(DashboardView, self).get(request, *args, **kwargs)

    def filter_date(self, queryset):
        initial_date = self.filters.get('initial_date', None)
        final_date = self.filters.get('final_date', None)
        updated_queryset = queryset
        if initial_date:
            for obj in queryset:
                    if obj.date.strftime('%Y-%m-%d') < initial_date:
                        updated_queryset.remove(obj)
        if final_date:
            for obj in queryset:
                if obj.date.strftime('%Y-%m-%d') > final_date:
                    updated_queryset.remove(obj)
        return queryset

    def get_context_data(self, **kwargs):
        queryset = Transaction.objects.filter(user=self.request.user)
        queryset = [ obj for obj in queryset]
        queryset = self.filter_date(queryset)

        ctx = super(DashboardView, self).get_context_data()
        ctx['filter_form'] = self.form_class

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
        date = [obj.date.strftime('%Y-%m-%d') for obj in queryset]

        ctx['breadcrumbs'] = 'DashboardView'
        ctx['queryset'] = {
            'names': json.dumps(names),
            'categories': json.dumps(categories),
            'types': json.dumps(types),
            'values': json.dumps(values),
            # 'dates': json.dumps(date),
        }
        return ctx