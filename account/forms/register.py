from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div
from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models.user import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'phone', 'email', 'password1', 'password2']

    phone = forms.CharField(max_length=20, label='Telefone', widget=forms.TextInput(attrs={'id':'phone-number'}))

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = self.build_layout()
        self.helper.add_input(Submit('submit', 'Salvar', css_class='btn btn-success'))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.count():
            raise forms.ValidationError('Esse endereço de email ja está sendo utilizado')
        else:
            return email

    def build_layout(self):
        return Layout(
            Div(
                Div('first_name', css_class='col-lg-6'),
                Div('last_name', css_class='col-lg-6'),
                css_class='row'
            ),
            Div(
                Div('username', css_class='col-lg-6'),
                Div('phone', css_class='col-lg-6'),
                css_class='row'
            ),
            Div(
                Div('email', css_class='col-lg-12'),
                css_class='row'
            ),
            Div(
                Div('password1', css_class='col-lg-12'),
                css_class='row'
            ),
            Div(
                Div('password2', css_class='col-lg-12'),
                css_class='row'
            )
        )