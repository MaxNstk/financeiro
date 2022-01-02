from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div
from django import forms

from account.models.user import User


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'phone', 'email', 'password', 'password2']

    first_name = forms.CharField(max_length=50, label='Primeiro Nome')
    last_name = forms.CharField(max_length=50, label='Sobrenome')
    username = forms.CharField(max_length=20, label='Nome de usuário', help_text='Nome único que será utilizado dentro do sistema')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=20, label='Telefone')
    password = forms.CharField(widget=forms.PasswordInput, label='Informe sua senha')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Repita sua senha')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = self.build_layout()
        self.helper.add_input(Submit('submit', 'Salvar'),)

    def clean_username(self):

        username = self.cleaned_data['username'].lower()
        user = User.objects.filter(username=username)
        if user.count():
            raise forms.ValidationError(
            "infelizmente o usuário "+username+" ja está sendo utilizado")
        return username

    def clean_email(self):

        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.count():
            raise forms.ValidationError(
                    "Infelizmente o email "+email+" ja está sendo utilizado")
        return email

    def clean_password2(self):

        cl = self.cleaned_data
        if cl['password'] != cl['password2']:
            raise forms.ValidationError(
                "As senhas informadas não são iguais")
        return cl['password2']

    def build_layout(self):
        return Layout(
            Div(
                Div('first_name', css_class='col-lg-5'),
                Div('last_name', css_class='col-lg-7'),
                css_class='row'
            ),
            Div(
                Div('username', css_class='col-lg-7'),
                Div('phone', css_class='col-lg-5'),
                css_class='row'
            ),
            Div(
                Div('email', css_class='col-lg-12'),
                css_class='row'
            ),
            Div(
                Div('password', css_class='col-lg-6'),
                Div('password2', css_class='col-lg-6'),
                css_class='row'
            )
        )