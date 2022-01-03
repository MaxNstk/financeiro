from account.forms import RegisterForm
from finances.forms.generic.custom_model_form import CustomModelForm


class UserUpdateForm(CustomModelForm):

    class Meta:
        model = RegisterForm
        exclude = ['password1','password2']