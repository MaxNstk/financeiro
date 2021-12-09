from django.urls import reverse_lazy
from django.views.generic import DeleteView

from finances.models import Category


class CategoryDeleteView(DeleteView):

    model = Category
    success_url = reverse_lazy('finances:category_list')
    template_name = 'finances/category/category_delete.html'