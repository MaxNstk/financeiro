from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):

        def __init__(self, *args, **kwargs):
            super(LoginForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.add_input(Submit('submit', 'Entrar'))