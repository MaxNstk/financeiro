
from django.http import JsonResponse

from finances.forms.transaction.multi_category_filter_form import MultiCategoryFilterForm
from finances.models import Transaction


class FilterCategories:

    @staticmethod
    def filter_unique_category(request):
        parameters = request.GET

        # getting the category
        category = parameters.get('cat_category', None)
        queryset = Transaction.objects.filter(user=request.user, category_id=category)

        # filtering type
        type = parameters.get('cat_type', None)
        queryset = queryset.filter(type=type)

        # filtering date
        initial_date = parameters.get('cat_initialDate', None)
        final_date = parameters.get('cat_finalDate', None)
        for obj in queryset:
            obj.date = obj.date.strftime('%Y-%m-%d')
        if initial_date:
            queryset = queryset.exclude(date__lt=initial_date)
        if final_date:
            queryset = queryset.exclude(date__gt=final_date)

        # filtering value
        value_lte = parameters.get('cat_valueLte', None)
        value_gte = parameters.get('cat_valueGte', None)
        if value_lte:
            queryset = queryset.exclude(value__gt=float(value_lte))
        if value_gte:
            queryset = queryset.exclude(value__lt=float(value_gte))

        total_value = 0
        queryset = queryset.order_by('-date')
        for obj in queryset:
            total_value += obj.value

        response = {}
        response['values'] = []
        response['dates'] = []
        response['transactions'] = []
        response['total_value'] = 0

        for obj in queryset:
            response['transactions'].append({'value':obj.value,
                                             'date': obj.date,
                                            'percentage': round((obj.value/total_value * 100), 2)})

            response['category'] = obj.category.name
            response['values'].append(obj.value)
            response['dates'].append(obj.date)
            response['total_value'] += obj.value

        return JsonResponse(response)

    @staticmethod
    def filter_multi_categories(request):
        categories = request.GET.getlist('category')
        params = request.GET
        queryset = Transaction.objects.filter(user=request.user)

        # filter the category
        if categories:
            querysets = []
            for category in categories:
                querysets.append(queryset.filter(category_id=category))
            queryset = Transaction.objects.none()
            for qs in querysets:
                queryset = queryset | qs

        for obj in queryset:
            obj.date = obj.date.strftime('%Y-%m-%d')

        initial_date = params.get('initial_date', None)
        final_date = params.get('final_date', None)
        if initial_date:
            queryset = queryset.exclude(date__lt=initial_date)
        if final_date:
            queryset = queryset.exclude(date__gt=final_date)

        for obj in queryset:
            obj.date = obj.date.strftime('%Y-%m-%d')

        type = params.get('type', None)
        queryset = queryset.filter(type=type)

        # get the total value from all the transactions in the queryset
        total_value = 0
        for obj in queryset:
            total_value += obj.value

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

            #filters the value
            value_lte = params.get('value_lte', None)
            value_gte = params.get('value_gte', None)
            if value_lte:
                if value > float(value_lte):
                    continue
            if value_gte:
                if value < float(value_gte):
                    continue

            categories.append({'name': category.name,
                               'value': value,
                               'percentage': round((value / total_value * 100), 2),
                               'color': category.color.lstrip('#')
                               })

        categories_names = []
        categories_values = []
        categories_percentages = []
        categories_colors = []
        for category in categories:
            for k, v in category.items():
                if k == 'name':
                    categories_names.append(v)
                elif k == 'value':
                    categories_values.append(v)
                elif k == 'percentage':
                    categories_percentages.append(v)
                elif k == 'color':
                    categories_colors.append(f'rgb{tuple(int(v[i:i+2], 16) for i in (0, 2, 4))}')

        response = {}
        response['categories'] = categories
        response['names'] = categories_names
        response['values'] = categories_values
        response['colors'] = categories_colors
        response['total_value'] = total_value
        return JsonResponse(response)