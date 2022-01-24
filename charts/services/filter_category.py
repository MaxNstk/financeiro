
from django.http import JsonResponse

from finances.models import Transaction


class FilterCategories:

    @staticmethod
    def filter_unique_category(request):
        parameters = request.GET

        # getting the category
        category = parameters.get('category', None)
        queryset = Transaction.objects.filter(user=request.user, category_id=category)

        # filtering type
        type = parameters.get('type', None)
        queryset = queryset.filter(type=type)

        # filtering date
        initial_date = parameters.get('initialDate', None)
        final_date = parameters.get('finalDate', None)
        for obj in queryset:
            obj.date = obj.date.strftime('%Y-%m-%d')
        if initial_date:
            queryset = queryset.exclude(date__lt=initial_date)
        if final_date:
            queryset = queryset.exclude(date__gt=final_date)

        # filtering value
        value_lte = parameters.get('valueLte', None)
        value_gte = parameters.get('valueGte', None)
        if value_lte:
            queryset = queryset.exclude(value__gt=float(value_lte))
        if value_gte:
            queryset = queryset.exclude(value__lt=float(value_gte))

        response = {}
        response['values'] = []
        response['dates'] = []

        for obj in queryset:
            response['category'] = obj.category.name
            response['values'].append(obj.value)
            response['dates'].append(obj.date)

        return JsonResponse(response)

    @staticmethod
    def filter_multi_categories(request):
        categories = request.GET.getlist('categories[]')
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

        initial_date = params.get('initialDate', None)
        final_date = params.get('finalDate', None)
        if initial_date:
            queryset = queryset.exclude(date__lt=initial_date)
        if final_date:
            queryset = queryset.exclude(date__gt=final_date)

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
            value_lte = params.get('valueLte', None)
            value_gte = params.get('valueGte', None)
            if value_lte:
                if value > float(value_lte):
                    continue
            if value_gte:
                if value < float(value_gte):
                    continue

            categories.append({'name': category.name,
                               'value': value,
                               'percentage': round((value / total_value * 100), 2)
                               })

        categories_names = []
        categories_values = []
        categories_percentages = []

        for category in categories:
            for k, v in category.items():
                if k == 'name':
                    categories_names.append(v)
                if k == 'value':
                    categories_values.append(v)
                if k == 'percentage':
                    categories_percentages.append(v)

        response = {}
        response['categories'] = categories
        response['names'] = categories_names
        response['values'] = categories_values
        response['percentages'] = categories_percentages

        return JsonResponse(response)