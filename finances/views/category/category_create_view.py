from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView

from finances.forms.category.category_form import CategoryForm
from finances.models import Category


class CategoryCreateView(CreateView):
    model = Category
    success_url = reverse_lazy('finances:category_list')
    form_class = CategoryForm
    template_name = 'finances/category/category_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(form.cleaned_data['name'])
        try:
            return super(CategoryCreateView, self).form_valid(form)
        except Exception as e:
            return self.form_invalid(form)