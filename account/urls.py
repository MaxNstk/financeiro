from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from account.forms.custom_login_form import LoginForm
from account.views.authentication.password_reset import CustomPasswordResetView
from account.views.authentication.register import RegisterView

app_name = 'account'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='account/login.html',form_class=LoginForm, success_url='home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='account:login'), name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    ]

