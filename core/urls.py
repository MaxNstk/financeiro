from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from django.conf import settings

from finances.views import HomeView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('finances/', include('finances.urls', namespace='finances')),
    path('charts/', include('charts.urls', namespace='charts')),
    path('', login_required(HomeView.as_view()), name='home'),
    path('api/v1/', include('api.urls', namespace='api'))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

