from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

from api.v1.viewsets.category_viewset import CategoryViewSet
from api.v1.viewsets.transaction_viewset import TransactionViewSet

app_name = 'api'

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('transaction', TransactionViewSet)
urlpatterns = [
    path('auth/', ObtainAuthToken.as_view(),name='auth'),
    *router.urls
    ]
