from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from finances.models import Category


class CategoryCreateForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {'user': forms.HiddenInput(),
                   'slug': forms.HiddenInput()}

    name = forms.CharField(label='Nome', max_length=50)
    description = forms.CharField(label='Descrição', max_length=500, widget=forms.Textarea())
    image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(CategoryCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Salvar'))