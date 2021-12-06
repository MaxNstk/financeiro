from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div
from django import forms

from finances.models import Wallet


class WalletCreateForm(forms.ModelForm):

    class Meta:
        model = Wallet
        fields = '__all__'
        widgets = {'user': forms.HiddenInput()}

    name = forms.CharField(label='Nome da Carteira', max_length=50)
    description = forms.CharField(label='Descrição', max_length=500, widget=forms.Textarea())
    balance = forms.FloatField(label='Saldo inicial da carteira')

    def __init__(self, *args, **kwargs):
        super(WalletCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

        )

        self.helper.add_input(Submit('submit', 'Salvar'))

    def build_layout(self):
        return Layout(
            Div(

            )
        )