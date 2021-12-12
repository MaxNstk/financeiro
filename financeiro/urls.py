from django.contrib import admin
from django.urls import path, include

from finances.views import HomeView



urlpatterns = [

    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('finances/', include('finances.urls', namespace='finances')),
    path('', HomeView.as_view(), name='home'),
]