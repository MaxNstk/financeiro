from crispy_forms.layout import Layout, Div
from django import forms
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from finances.forms.generic.custom_model_form import CustomModelForm
from finances.models import Category


class CategoryForm(CustomModelForm):

    class Meta:
        model = Category
        exclude = ['user', 'slug']

    name = forms.CharField(label=mark_safe('<b>Nome</b>'), max_length=50)
    description = forms.CharField(label='Descrição', max_length=500, widget=forms.Textarea(), required=False)

    def clean_name(self):

        name = self.cleaned_data['name']
        try:
            if Category.objects.get(slug=slugify(name)).exists():
                raise forms.ValidationError(
                    'Ja existe uma categoria com esse nome')
        except:
            pass
        return name

    def build_layout(self):
        return Layout(
            Div(
                Div('name', css_class='col-lg-12'),
                css_class='row'
            ),
            Div(
                Div('description', css_class='col-lg-12'),
                css_class='row'
            )
        )