from django.urls import reverse_lazy

from finances.models import Category
from finances.views.generic.custom_delete_view import CustomDeleteView


class CategoryDeleteView(CustomDeleteView):

    model = Category
    success_url = reverse_lazy('finances:category_list')
    template_name = 'finances/category/category_delete.html'