from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div
from django import forms
from django.utils.safestring import mark_safe

from finances.models import Transaction


class TransactionCreateForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {'user': forms.HiddenInput()}

    name = forms.CharField(label=mark_safe('<b> Nome </b>'), max_length=50)
    value = forms.FloatField(label=mark_safe('<b> Valor da Transação </b>'))
    image = forms.ImageField(label='Imagem', required=False)
    description = forms.CharField(label='Descrição', max_length=500, widget=forms.Textarea(), required=False)
    date = forms.DateField(label=mark_safe('<b> Data </b>'))

    def __init__(self, *args, **kwargs):
        super(TransactionCreateForm, self).__init__(*args, **kwargs)
        self.fields['wallet'].label = mark_safe('<b> Carteira </b>')
        self.fields['category'].label = mark_safe('<b> Categoria </b>')
        self.fields['type'].label = mark_safe('<b> Tipo da Transação </b>')
        self.helper = FormHelper()
        self.helper.layout = self.build_layout()
        self.helper.add_input(Submit('submit', 'Salvar'))

    def build_layout(self):
        return Layout(
            Div(
                Div('name', css_class='col-lg-8'),
                Div('type', css_class='col-lg-4'),
                css_class= 'row'
            ),
            Div(
                Div('value', css_class='col-lg-4'),
                Div('wallet', css_class='col-lg-4'),
                Div('category', css_class='col-lg-4'),
                css_class='row'
            ),
            Div(
                Div('date', css_class='col-lg-4'),
                Div('image', css_class='col-lg-8'),
                css_class='row'
            ),
            Div(
                Div('description', css_class='col-lg-12'),
                css_class='row'
            )
        )
