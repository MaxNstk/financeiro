from django.urls import path

from account.views.authentication.register import RegisterView

app_name = 'account'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]