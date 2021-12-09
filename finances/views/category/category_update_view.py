from django.urls import reverse_lazy
from django.views.generic import UpdateView

from finances.forms.category.category_form import CategoryForm
from finances.models import Category


class CategoryUpdateView(UpdateView):

    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('finances:category_list')
    template_name = 'finances/category/category_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super(CategoryUpdateView, self).form_valid(form)
        except Exception as e:
            return e