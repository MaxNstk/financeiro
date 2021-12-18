from account.forms.register import RegisterForm
from account.models import User
from finances.views.generic.custom_create_view import CustomCreateView


class RegisterView(CustomCreateView):
    model = User
    form_class = RegisterForm
    success_url = '/'
    template_name = 'account/register.html'
    breadcrumbs = 'Criação de Usuário'
