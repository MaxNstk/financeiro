from crispy_forms.layout import Layout, Div, Field
from django.forms import ChoiceField, FloatField, DateField

from finances.forms.generic.custom_model_form import CustomModelForm
from finances.models import Category, Transaction
from finances.forms.transaction.transaction_form import DateInput


class TransactionFilterForm(CustomModelForm):

    class Meta:
        model = Transaction
        fields = ['category', 'type']

    initial_date = DateField(label='Data inicial', widget=DateInput())
    final_date = DateField(label='Data final', widget=DateInput())

    value__gte = FloatField(label='Valores maiores que')
    value__lte = FloatField(label='Valores menores que')
    type = ChoiceField(choices=[('1', 'Renda'), ('2', 'Despesa')], label= 'Tipo')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TransactionFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
        self.fields['category'].queryset = Category.objects.filter(user=user)
        self.fields['category'].label = 'Categoria'
        self.helper.form_method = 'get'

    def build_layout(self):
        return Layout(
            Div(
                Div(Field('initial_date'), css_class='col-lg-3'),
                Div(Field('final_date'), css_class='col-lg-3'),
                Div(Field('value__gte'), css_class='col-lg-3'),
                Div(Field('value__lte'), css_class='col-lg-3'),
                css_class='row'
            ),
            Div(
                Div(Field('category'), css_class='col-lg-6'),
                Div(Field('type'), css_class='col-lg-6'),
                css_class='row'
            )
        )