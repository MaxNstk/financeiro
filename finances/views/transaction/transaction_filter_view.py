from django.views.generic import FormView

from finances.forms.transaction.transaction_filter_form import TransactionFilterForm


class TransactionFilterView(FormView):

    form_class = TransactionFilterForm
    template_name = 'generic/dashboard.html'
    filters = {}

    def get(self, request, *args, **kwargs):
        self.filters = dict(map(lambda k: (k, request.GET[k]), request.GET))
        if 'csrfmiddlewaretoken' in self.filters:
            self.filters.pop('csrfmiddlewaretoken')
        return super(TransactionFilterView, self).get(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(TransactionFilterView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_initial(self):

        # cleaning filters
        for field in self.form_class.base_fields.items():
            field[1].initial = None

        # setting filters
        for key, value in self.filters.items():
            if key == 'submit' or key == 'len':
                continue
            self.form_class.base_fields[key].initial = value
        return self.filters

    def filter_date(self, queryset):
        initial_date = self.filters.get('initial_date', None)
        final_date = self.filters.get('final_date', None)
        for obj in queryset:
            obj.date = obj.date.strftime('%Y-%m-%d')

        if initial_date:
            queryset = queryset.exclude(date__lt=initial_date)
        if final_date:
            queryset = queryset.exclude(date__gt=final_date)

        return queryset

    def filter_category(self, queryset):
        category = self.filters.get('category', None)
        if category:
            queryset = queryset.filter(category_id=category)
        return queryset

    def filter_value(self, queryset):
        value_lte = self.filters.get('value_lte', None)
        value_gte = self.filters.get('value_gte', None)

        if value_lte:
            queryset = queryset.exclude(value__gt=value_lte)
        if value_gte:
            queryset = queryset.exclude(value__lt=value_gte)

        return queryset

    def filter_type(self, queryset):
        type = self.filters.get('type', None)
        queryset = queryset.filter(type=type)
        return queryset
