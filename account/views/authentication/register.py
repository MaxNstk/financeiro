from account.forms.register import RegisterForm
from account.models import User
from finances.views.generic.custom_create_view import CustomCreateView


class RegisterView(CustomCreateView):
    model = User
    form_class = RegisterForm
    success_url = '/'
    template_name = 'account/register.html'

    breadcrumbs = 'Criação de Usuário'

    # def form_valid(self, form):
    #     if form.is_valid():
    #         user = RegisterForm.save(commit=False)
    #         user.username = RegisterForm.cleaned_data['username']
    #         user.email = RegisterForm.cleaned_data['email']
    #         user.set_password(RegisterForm.cleaned_data['password'])
    #         user.is_active = False
    #         user.save()