
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit, Button, ButtonHolder
from django.forms import ChoiceField, FloatField, DateField, ModelForm
from django.urls import reverse_lazy
from django_filters.fields import ModelMultipleChoiceField

from finances.models import Category, Transaction
from finances.forms.transaction.transaction_form import DateInput


class TransactionFilterForm(ModelForm):

    class Meta:
        model = Transaction
        fields = ['category', 'type']

    initial_date = DateField(label='Datas iguais e posteriores à:', widget=DateInput())
    final_date = DateField(label='Datas iguais e anteriores à:', widget=DateInput())
    value_lte = FloatField(label='Valores menores que:')
    value_gte = FloatField(label='Valores maiores que:')
    type = ChoiceField(choices=[('1', 'Renda'), ('2', 'Despesa')], label= 'Tipo')
    category = ModelMultipleChoiceField(queryset=None, label='Categoria')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        self.base_fields['category'].queryset = Category.objects.filter(user=user)
        self.base_fields['category'].label = 'Categoria'
        self.base_fields['type'].initial = '2'

        super(TransactionFilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = self.build_layout()
        for field in self.fields.values():
            field.required = False
        self.helper.form_method = 'get'


    def build_layout(self):
        return Layout(
            Div(
                Div(Field('initial_date'), css_class='col-lg-3'),
                Div(Field('final_date'), css_class='col-lg-3'),
                Div(Field('value_lte'), css_class='col-lg-3'),
                Div(Field('value_gte'), css_class='col-lg-3'),
                css_class='row', style='margin-bottom: 1%;'
            ),
            Div(
                Div(Field('category'), css_class='col-lg-6'),
                Div(Field('type'), css_class='col-lg-6'),
                css_class='row', style='margin-bottom: 1%;'
            ),
            ButtonHolder(
                Submit('submit', 'Filtrar', css_class='btn btn-primary',),
                Button('cancel', 'Remover Filtros', css_class='btn-primary',
                       onclick=f"window.location.href = '{reverse_lazy('charts:dashboard')}'"),
            ),

        )
