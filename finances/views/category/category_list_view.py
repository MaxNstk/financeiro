from django.views.generic import ListView

from finances.models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'finances/category/category_list.html'