from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView
from django.urls import path

from account.forms.custom_login_form import LoginForm
from account.views.authentication.activate import activate_account
from account.views.authentication.password_reset import CustomPasswordResetView
from account.views.authentication.register import RegisterView
from account.views.profile import ProfileView
# from account.views.profile_update import ProfileUpdateView

app_name = 'account'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='account/login.html',form_class=LoginForm, success_url='home'), name='login'),
    path('logout/', login_required(LogoutView.as_view(next_page='account:login')), name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),

    path('profile/', login_required(ProfileView.as_view()), name='profile'),
    path('activate/<slug:uidb64>/<slug:token>)/', activate_account, name='activate'),
    # path('profile_update/', ProfileUpdateView.as_view(), name='profile_update'),
    ]