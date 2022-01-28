
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Button, ButtonHolder
from django.forms import ChoiceField, FloatField, DateField, Form
from django.urls import reverse_lazy
from django_filters.fields import ModelMultipleChoiceField

from finances.forms.transaction.transaction_form import DateInput


class MultiCategoryFilterForm(Form):

    initial_date = DateField(label='Datas iguais e posteriores à:', widget=DateInput())
    final_date = DateField(label='Datas iguais e anteriores à:', widget=DateInput())
    value_lte = FloatField(label='Valores menores que:')
    value_gte = FloatField(label='Valores maiores que:')
    type = ChoiceField(choices=[('1', 'Renda'), ('2', 'Despesa')], label= 'Tipo')
    category = ModelMultipleChoiceField(queryset=None, label='Categorias')

    def __init__(self, *args, **kwargs):
        self.base_fields['category'].label = 'Categoria'
        self.base_fields['type'].initial = '2'

        super(MultiCategoryFilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {'id':'multi-categories-form'}
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
                Button('submit', 'Filtrar', css_class='btn btn-primary', css_id='multi_categories_submit'),
                Button('cancel', 'Remover Filtros', css_class='btn-primary',
                       onclick=f"window.location.href = '{reverse_lazy('charts:dashboard')}'"),
            ),

        )
