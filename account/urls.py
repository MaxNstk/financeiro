from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from account.views.authentication.password_reset import CustomPasswordResetView
from account.views.authentication.register import RegisterView

app_name = 'account'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='account/login.html', success_url='home'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    ]

