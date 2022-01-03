from django.core.mail import send_mail
from django.urls import reverse_lazy

from account.forms.register import RegisterForm
from account.models import User
from financeiro import settings
from finances.views.generic.custom_create_view import CustomCreateView


class RegisterView(CustomCreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/register.html'
    breadcrumbs = 'Criação de Usuário'

    def form_valid(self, form):
        send_mail(subject='Thank you for registering to our site',
        message=' it  means a world to us ',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[form.data['email']])
        return super(RegisterView, self).form_valid(form)