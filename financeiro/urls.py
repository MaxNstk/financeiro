from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from finances.views import HomeView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', login_required(include('account.urls', namespace='account'))),
    path('finances/', login_required(include('finances.urls', namespace='finances'))),
    path('', HomeView.as_view(), name='home'),
]