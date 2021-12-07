from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div
from django import forms
from django.utils.safestring import mark_safe


from finances.models import Wallet


class WalletCreateForm(forms.ModelForm):

    class Meta:
        model = Wallet
        exclude = ['user']

    name = forms.CharField(label=mark_safe('<b>Nome da Carteira</b>'), max_length=50)
    description = forms.CharField(label='Descrição', max_length=500, widget=forms.Textarea(), required=False)
    balance = forms.FloatField(label=mark_safe('<b>Saldo inicial da carteira</b>'))

    def __init__(self, *args, **kwargs):
        super(WalletCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = self.build_layout()
        self.helper.add_input(Submit('submit', 'Salvar'))

    def build_layout(self):
        return Layout(
            Div(
                Div('name', css_class='col-lg-8'),
                Div('balance', css_class='col-lg-4'),
                css_class='row'
            ),
            Div(
                Div('description', css_class='col-lg-12'),
                css_class='row'
            )
        )
