from django.contrib.auth.views import PasswordResetView

from account.forms.password_reset import CustomPasswordResetForm


class CustomPasswordResetView(PasswordResetView):

    template_name = 'account/password_reset.html'
    form_class = CustomPasswordResetForm