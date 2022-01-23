from django.contrib.auth.decorators import login_required
from django.urls import path

from charts.services.filter_categories import FilterCategories
from charts.views.dashborad import DashboardView

app_name = 'charts'

urlpatterns = [

    path('dashboard', login_required(DashboardView.as_view()), name='dashboard'),

    # services
    path('filter_categoriees', FilterCategories.filter_categories, name='filter_categoriees')
]