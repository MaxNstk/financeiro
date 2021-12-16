from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from account.views.authentication.register import RegisterView

app_name = 'account'

urlpatterns = [
    path('register/', RegisterView.as_view(template_name='account/register.html'), name='register'),
    path('login/', LoginView.as_view(template_name='account/login.html', success_url='home'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    ]

