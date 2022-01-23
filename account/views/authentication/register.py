from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from account.forms.register import RegisterForm
from account.models import User
from account.tokens.activation_token import activation_token
from financeiro import settings
from finances.views.generic.custom_create_view import CustomCreateView


class RegisterView(CustomCreateView):

    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/register.html'
    breadcrumbs = 'Criação de Usuário'

    def form_valid(self, form):
        form.instance.is_active = False
        super(RegisterView, self).form_valid(form)
        try:
            user = self.object
            current_site = get_current_site(self.request)
            user_id= force_bytes(user.id)
            user_id = urlsafe_base64_encode(user_id)
            token = activation_token.make_token(user)
            send_mail(subject='Ativação de conta',
            message=render_to_string('account/activation_email.html', {
                'user': form.instance,
                'domain': current_site.domain,
                'uid': user_id,
                'token':token
            }),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[form.data['email']])
            return render(self.request, 'account/activation_send.html')
        except Exception as e:
            print(e)