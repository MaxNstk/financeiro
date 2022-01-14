from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, reverse_lazy

from account.forms.custom_login_form import LoginForm
from account.forms.password_set import CustomSetPasswordForm
from account.views.authentication.activate import activate_account
from account.views.authentication.password_reset import CustomPasswordResetView
from account.views.authentication.register import RegisterView
from account.views.profile import ProfileView
# from account.views.profile_update import ProfileUpdateView

app_name = 'account'

urlpatterns = [
    # login and logout
    path('login/', LoginView.as_view(template_name='account/login.html', form_class=LoginForm, success_url='home'),
         name='login'),
    path('logout/', login_required(LogoutView.as_view(next_page='account:login')), name='logout'),

    # register and activate
    path('register/', RegisterView.as_view(), name='register'),
    path('activate/<slug:uidb64>/<slug:token>)/', activate_account, name='activate'),

    # password reset
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<str:uidb64>/<str:token>/',
         PasswordResetConfirmView.as_view(
         form_class=CustomSetPasswordForm,
         template_name='account/password_reset_confirm.html',
         success_url=reverse_lazy('account:password_reset_end')),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='account/password_reset_end.html'),
         name='password_reset_end'),

    path('profile/', login_required(ProfileView.as_view()), name='profile'),
    # path('profile_update/', ProfileUpdateView.as_view(), name='profile_update'),
    ]