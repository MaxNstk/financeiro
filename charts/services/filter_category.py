from django.db.models import Sum
from django.http import JsonResponse

from finances.models import Transaction


class FilterCategories:

    @staticmethod
    def filter_unique_category(request):
        params = request.GET

        # getting the queryset based on the category
        queryset = Transaction.objects.filter(user=request.user, category_id=params['cat_category'])

        # filtering the type
        queryset = queryset.filter(type=params['cat_type'])

        # filtering the date
        if params.get('cat_initial_date', None):
            queryset = queryset.exclude(date__lt=params['cat_initial_date'])
        if params.get('cat_final_date', None):
            queryset = queryset.exclude(date__gt=params['cat_final_date'])

        # filtering the value
        if params.get('cat_value_lte', None):
            queryset.exclude(value__gt=params['cat_value_lte'])
        if params.get('cat_value_gte', None):
            queryset.exclude(value__lt=params['cat_value_gte'])

        # structuring the response
        queryset = queryset.order_by('-date')
        response = {}
        response['values'] = []
        response['dates'] = []
        response['transactions'] = []
        response['total_value'] = queryset.aggregate(Sum('value'))['value__sum']

        for obj in queryset:
            response['transactions'].append({'value':obj.value,
                                             'date': obj.date,
                                            'percentage': round((obj.value/response['total_value'] * 100), 2)})
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

        # filtering the category
        if categories:
            querysets = []
            for category in categories:
                querysets.append(queryset.filter(category_id=category))
            queryset = Transaction.objects.none()
            for qs in querysets:
                queryset = queryset | qs

        # filtering the date
        if params.get('initial_date', None):
            queryset = queryset.exclude(date__lt=params['initial_date'])
        if params.get('final_date', None):
            queryset = queryset.exclude(date__gt=params['final_date'])

        #filtering the type
        queryset = queryset.filter(type=params['type'])
        total_value = queryset.aggregate(Sum('value'))['value__sum']

        # get all the categories of the queryset and creates a list of it
        categories = []
        for obj in queryset:
            categories.append(obj.category)
        categories = set(categories)
        qs_categories = []
        for category in categories:
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

            qs_categories.append({'name': category.name,
                               'value': value,
                               'percentage': round((value / total_value * 100), 2),
                               'color': category.color.lstrip('#')
                               })

        # structuring the response
        categories_names = []
        categories_values = []
        categories_percentages = []
        categories_colors = []

        for category in qs_categories:
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
        response['categories'] = qs_categories
        response['names'] = categories_names
        response['values'] = categories_values
        response['colors'] = categories_colors
        response['total_value'] = total_value

        return JsonResponse(response)