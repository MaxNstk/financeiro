
from django.http import JsonResponse

from finances.models import  Transaction


class FilterCategories:

    @staticmethod
    def filter_categories(request):
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