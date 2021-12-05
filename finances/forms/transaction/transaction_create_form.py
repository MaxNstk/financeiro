from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from finances.models import Transaction


class TransactionCreateForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {'user': forms.HiddenInput(),}

    def __init__(self, *args, **kwargs):
        super(TransactionCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Salvar'))