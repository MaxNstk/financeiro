from datetime import datetime

from crispy_forms.layout import Layout, Div
from django import forms
from django.utils.safestring import mark_safe

from finances.forms.generic.custom_model_form import CustomModelForm
from finances.models import Transaction, Category


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
        self.fields['category'].label = mark_safe('Categoria')
        self.fields['category'].required = False
        self.fields['category'].queryset = Category.objects.filter(user=self.user).exclude(name='Descategorizado')
        self.fields['type'].label = mark_safe('<b> Tipo da Transação </b>')

    value = forms.FloatField(label=mark_safe('<b> Valor da Transação </b>'))
    description = forms.CharField(label='Descrição', max_length=500, widget=forms.Textarea(), required=False)
    date = forms.DateField(label=mark_safe('<b> Data </b>'), initial=datetime.now().strftime('%Y-%m-%d'), widget=DateInput())

    def clean_value(self):

        cl = self.cleaned_data

        # validates if the transaction value is bigger than 0
        value = cl['value']
        if value <= 0:
            raise forms.ValidationError('Não é possível adicionar valores igual à zero ou inferiores. '
                                        'Caso necessário mude o Tipo da Transação')

        return value

    def build_layout(self):
        return Layout(
            Div(
                Div('category', css_class='col-lg-3'),
                Div('type', css_class='col-lg-3'),
                Div('value', css_class='col-lg-3'),
                Div('date', css_class='col-lg-3'),
                css_class='row'
            ),
            Div(
                Div('description', css_class='col-lg-12'),
                css_class='row'
            )
        )
