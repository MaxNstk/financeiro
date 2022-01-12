from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy

from account.forms.password_reset import CustomPasswordResetForm


class CustomPasswordResetView(PasswordResetView):

    template_name = 'account/password_reset.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('account:password_reset_done')