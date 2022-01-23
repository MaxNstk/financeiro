from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Button, ButtonHolder
from django.forms import ChoiceField, FloatField, DateField, Form, ModelChoiceField
from django.urls import reverse_lazy

from finances.forms.transaction.transaction_form import DateInput


# Form that filters categories based on the transactions
from finances.models import Category


class TransactionCategoryFilterForm(Form):

    cat_initial_date = DateField(label='Datas iguais e posteriores à:', widget=DateInput())
    cat_final_date = DateField(label='Datas iguais e anteriores à:', widget=DateInput())
    cat_value_lte = FloatField(label='Valores menores que:')
    cat_value_gte = FloatField(label='Valores maiores que:')
    cat_type = ChoiceField(choices=[('1', 'Renda'), ('2', 'Despesa')], label='Tipo')
    cat_category = ModelChoiceField(queryset=None, label='Categoria')

    def __init__(self, *args, **kwargs):
        self.base_fields['cat_type'].initial = '2'
        super(TransactionCategoryFilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = self.build_layout()
        for field in self.fields.values():
            field.required = False
        self.helper.form_method = 'get'

    def build_layout(self):
        return Layout(
            Div(
                Div(Field('cat_category'), css_class='col-lg-6'),
                Div(Field('cat_type'), css_class='col-lg-6'),
                css_class='row', style='margin-bottom: 1%;'
            ),
            Div(
                Div(Field('cat_initial_date'), css_class='col-lg-3'),
                Div(Field('cat_final_date'), css_class='col-lg-3'),
                Div(Field('cat_value_lte'), css_class='col-lg-3'),
                Div(Field('cat_value_gte'), css_class='col-lg-3'),
                css_class='row', style='margin-bottom: 1%;'
            ),
            ButtonHolder(
                Button('submit', 'Filtrar', css_class='btn btn-primary', css_id='category_filter_submit'),
                Button('cancel', 'Remover Filtros', css_class='btn-primary', css_id='category_filter_cancel',
                       onclick=f"window.location.href = '{reverse_lazy('charts:dashboard')}'"),
            ),

        )
