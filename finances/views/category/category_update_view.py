from django.urls import reverse_lazy

from finances.forms.category.category_form import CategoryForm
from finances.models import Category
from finances.views.generic.custom_update_view import CustomUpdateView


class CategoryUpdateView(CustomUpdateView):

    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('finances:category_list')
    template_name = 'generic/generic_form.html'

    breadcrumbs = 'Atualização de Categoria'

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super(CategoryUpdateView, self).form_valid(form)
        except Exception as e:
            return e