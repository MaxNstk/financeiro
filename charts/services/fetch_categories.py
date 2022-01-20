from django.http import JsonResponse

from finances.models import Category, Transaction


class FetchCategories:

    @staticmethod
    def fetch_categories(request):
        category_search = request.GET.get('term', '')
        categories = Category.objects.filter(name__icontains=category_search)
        transactions = []
        for obj in Transaction.objects.filter(user=request.user):
            if obj.category in categories:
                categories.append({'id': obj.id,
                                   'text': obj.name})
        return JsonResponse({'results':categories})