import datetime
from django.views.generic import TemplateView

from finances.forms.transaction.multi_category_filter_form import MultiCategoryFilterForm
from finances.forms.transaction.unique_category_filter_form import UniqueCategoryFilterForm

from finances.models import Category


class DashboardView(TemplateView):

    multi_categories_form = MultiCategoryFilterForm
    unique_category_form = UniqueCategoryFilterForm
    template_name = 'generic/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super(DashboardView, self).get_context_data()

        # setting the available categories in the form
        available_categories = Category.objects.filter(user=self.request.user)

        MultiCategoryFilterForm.base_fields['category'].queryset = available_categories
        UniqueCategoryFilterForm.base_fields['cat_category'].queryset = available_categories

        # todo fazer metodo para trazer a categoria com mais transações
        UniqueCategoryFilterForm.base_fields['cat_category'].initial = Category.objects.get(user=self.request.user, name='Mercado')

        ctx['multi_categories_form'] = MultiCategoryFilterForm
        ctx['unique_category_form'] = UniqueCategoryFilterForm
        return ctx