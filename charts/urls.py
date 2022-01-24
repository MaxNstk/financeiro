from django.contrib.auth.decorators import login_required
from django.urls import path

from charts.services.filter_category import FilterCategories
from charts.views.dashboard import DashboardView

app_name = 'charts'

urlpatterns = [

    path('dashboard', login_required(DashboardView.as_view()), name='dashboard'),

    # services
    path('filter_unique_category', FilterCategories.filter_unique_category, name='filter_unique_category'),
    path('filter_multi_categories', FilterCategories.filter_multi_categories, name='filter_multi_categories'),
]