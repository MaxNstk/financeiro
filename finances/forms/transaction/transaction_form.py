from datetime import datetime

from crispy_forms.layout import Layout, Div
from django import forms
from django.utils.safestring import mark_safe

from finances.forms.generic.custom_model_form import CustomModelForm
from finances.models import Transaction, Wallet, Category


class DateInput(forms.DateInput):
    input_type = 'date'


class TransactionForm(CustomModelForm):
    user = None

    class Meta:
        model = Transaction
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['category'].label = mark_safe('<b> Categoria </b>')
        self.fields['category'].required = False
        self.fields['category'].queryset = Category.objects.filter(user=self.user)
        self.fields['wallet'].label = mark_safe('<b> Carteira </b>')
        self.fields['wallet'].queryset = Wallet.objects.filter(user=self.user)
        self.fields['wallet'].initial = self.get_main_wallet(self.user)
        self.fields['type'].label = mark_safe('<b> Tipo da Transação </b>')

    name = forms.CharField(label=mark_safe('<b> Nome </b>'), max_length=50)
    value = forms.FloatField(label=mark_safe('<b> Valor da Transação </b>'))
    description = forms.CharField(label='Descrição', max_length=500, widget=forms.Textarea(), required=False)
    date = forms.DateField(label=mark_safe('<b> Data </b>'), initial=datetime.now(), widget=DateInput())

    @staticmethod
    def get_main_wallet(user):
        wallet = Wallet.objects.filter(user=user, main=True)
        if wallet.count():
            return wallet[0]
        else:
            return None

    def clean_value(self):

        cl = self.cleaned_data

        # validates if the transaction value is bigger than 0
        value = cl['value']
        if value <= 0:
            raise forms.ValidationError('Não é possível adicionar valores igual à zero ou inferiores. '
                                        'Caso necessário mude o Tipo da Transação')
        wallet = cl['wallet']
        current_transaction = self.cleaned_data

        # check if is a update
        if self.instance.id:
            old_transaction = Transaction.objects.get(id=self.instance.id)

            # decreases the old value from the wallet balance
            if old_transaction.type == Transaction.CREDIT:
                wallet.balance -= old_transaction.value
            else:
                wallet.balance += old_transaction.value

        if current_transaction['type'] == Transaction.EXPENSE:

            # if expense, check if the wallet has sufficient money in the balance
            if wallet.balance - current_transaction['value'] < 0:
                raise forms.ValidationError(
                    'Valor excede o limite. O saldo disponível da carteira é: R$: ' + str(wallet.balance))

        return value

    def build_layout(self):
        return Layout(
            Div(
                Div('name', css_class='col-lg-8'),
                Div('type', css_class='col-lg-4'),
                css_class='row'
            ),
            Div(
                Div('value', css_class='col-lg-3'),
                Div('wallet', css_class='col-lg-3'),
                Div('category', css_class='col-lg-3'),
                Div('date', css_class='col-lg-3'),
                css_class='row'
            ),
            Div(
                Div('description', css_class='col-lg-12'),
                css_class='row'
            )
        )
