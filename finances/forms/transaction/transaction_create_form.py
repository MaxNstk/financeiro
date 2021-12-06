from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import ModelChoiceField

from finances.models import Transaction


class TransactionCreateForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {'user': forms.HiddenInput()}

    name = forms.CharField(label='Nome', max_length=50)
    value = forms.FloatField(label='Valor da transação')
    image = forms.ImageField(label='Imagem')
    description = forms.CharField(label='Descrição', max_length=500, widget=forms.Textarea())
    date = forms.DateField(label='Data')

    def __init__(self, *args, **kwargs):
        super(TransactionCreateForm, self).__init__(*args, **kwargs)
        self.fields['wallet'].label = 'Carteira'
        self.fields['category'].label = 'Categoria'
        self.fields['type'].label = 'Tipo da Transação'
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Salvar'))