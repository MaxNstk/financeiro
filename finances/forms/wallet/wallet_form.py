from crispy_forms.layout import Layout, Div
from django import forms
from django.utils.safestring import mark_safe

from finances.forms.generic.custom_model_form import CustomModelForm
from finances.models import Wallet


class Walletform(CustomModelForm):

    class Meta:
        model = Wallet
        exclude = ['user', 'initial_balance']

    name = forms.CharField(label=mark_safe('<b>Nome da Carteira</b>'), max_length=50)
    description = forms.CharField(label='Descrição', max_length=500, widget=forms.Textarea(), required=False)
    balance = forms.FloatField(label=mark_safe('<b>Saldo inicial da carteira</b>'))
    main = forms.BooleanField(label=mark_safe(' Carteira principal '), required=False)

    def clean_balance(self):
        if self.cleaned_data['balance'] < 0:
            raise forms.ValidationError("O saldo inicial deve ser maior ou igual a Zero")
        return self.cleaned_data['balance']

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
            ),
            Div(
                Div('main', css_class='col-lg-12'),
                css_class='row'
            )
        )