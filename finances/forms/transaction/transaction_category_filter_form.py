from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit, Button, ButtonHolder
from django.forms import ChoiceField, FloatField, DateField, ModelForm
from django.urls import reverse_lazy

from finances.models import Category, Transaction
from finances.forms.transaction.transaction_form import DateInput


# Form that filters categories based on the transactions
class TransactionFilterForm(ModelForm):

    class Meta:
        model = Transaction
        fields = ['category', 'type']

    cat_initial_date = DateField(label='Datas iguais e posteriores à:', widget=DateInput())
    cat_final_date = DateField(label='Datas iguais e anteriores à:', widget=DateInput())
    cat_value_lte = FloatField(label='Valores menores que:')
    cat_value_gte = FloatField(label='Valores maiores que:')
    cat_type = ChoiceField(choices=[('1', 'Renda'), ('2', 'Despesa')], label= 'Tipo')

    spe_value_lte = FloatField(label='Valores menores que:')

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
                Div(Field('cat_initial_date'), css_class='col-lg-3'),
                Div(Field('cat_final_date'), css_class='col-lg-3'),
                Div(Field('cat_value_lte'), css_class='col-lg-3'),
                Div(Field('cat_value_gte'), css_class='col-lg-3'),
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
