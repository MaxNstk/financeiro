from django.contrib.auth.decorators import login_required
from django.urls import path

from charts.services.fetch_categories import FetchCategories
from charts.views.dashborad import DashboardView

app_name = 'charts'

urlpatterns = [

    path('dashboard', login_required(DashboardView.as_view()), name='dashboard'),

    # services
    path('fetch_categories', FetchCategories.fetch_categories, name='fetch_categories')
]