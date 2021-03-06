import datetime

from finances.models import Transaction


class TransactionFilterView:

    filters = {}
    categories = None

    def get(self, request, *args, **kwargs):
        self.filters = dict(map(lambda k: (k, request.GET[k]), request.GET))
        self.categories = request.GET.getlist('category')
        if 'csrfmiddlewaretoken' in self.filters:
            self.filters.pop('csrfmiddlewaretoken')
        self.get_initial()
        if not self.filters.get('initial_date', None):
            self.filters['initial_date'] = (datetime.datetime.now() - datetime.timedelta(30)).strftime('%Y-%m-%d')
        if not self.filters.get('type', None):
            self.filters['type'] = '2'
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
        new_filters = {}
        for key, value in self.filters.items():
            if key == 'submit' or key == 'len':
                continue
            new_filters[key] = value
            self.form_class.base_fields[key].initial = value
        if self.categories:
            self.form_class.base_fields['category'].initial = self.categories
            new_filters['category'] = self.categories
        return new_filters

    def filter_date(self, queryset):
        for obj in queryset:
            obj.date = obj.date.strftime('%Y-%m-%d')

        initial_date = self.filters.get('initial_date', None)
        final_date = self.filters.get('final_date', None)

        if initial_date:
            queryset = queryset.exclude(date__lt=initial_date)
        if final_date:
            queryset = queryset.exclude(date__gt=final_date)

        for obj in queryset:
            obj.date = obj.date.strftime('%d-%m-%Y')

        return queryset

    def filter_category(self, queryset):
        if self.categories:
            querysets = []
            for category in self.categories:
                querysets.append(queryset.filter(category_id=category))
            queryset = Transaction.objects.none()
            for qs in querysets:
                queryset = queryset | qs
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
