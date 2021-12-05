from django.utils.text import slugify
from django.views.generic import CreateView

from finances.forms.category.category_create_form import CategoryCreateForm
from finances.models import Category


class CategoryCreateView(CreateView):
    model = Category
    success_url = '/'
    form_class = CategoryCreateForm
    template_name = 'finances/category/category_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(form.cleaned_data['name'])
        try:
            return super(CategoryCreateView, self).form_valid(form)
        except Exception as e:
            return self.form_invalid(form)