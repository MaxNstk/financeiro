from django_filters import FilterSet

from finances.models import Category


class CategoryFilter(FilterSet):

    class Meta:
        model = Category
        fields = {'name': ['icontains']}