from finances.models import Category
from finances.views.generic.custom_list_view import CustomListView


class CategoryListView(CustomListView):
    model = Category
    template_name = 'finances/category/category_list.html'
    breadcrumbs = 'Criação de Categoria'
