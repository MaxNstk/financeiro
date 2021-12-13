from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django import forms

from account.models.user import User
from finances.forms.generic.custom_model_form import CustomModelForm


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'phone', 'email']

    username = forms.CharField(max_length=20, label='Usuário')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=20, label='Telefone')
    password = forms.CharField(widget=forms.PasswordInput, label='Informe sua senha')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Repita sua senha')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.layout = self.build_layout()
        self.helper.add_input(Submit('submit', 'Salvar'))

    def clean_username(self):

        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
            "infelizmente o usuário "+username+" ja está sendo utilizado")
        return username

    def clean_email(self):

        email = self.cleaned_data['email']
        if User.objects.get(email=email):
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
        return {}