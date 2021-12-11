from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django import forms
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

class CustomModelForm(forms.ModelForm):

    def get_reverse_url(self):
        model = self._meta.model._meta.model_name.replace(' ', '_')
        return reverse_lazy(f'finances:{model}_list')

    def get_delete_url(self):
        model = self._meta.model._meta.model_name.replace(' ', '_')
        return reverse_lazy(f'finances:{model}_delete', kwargs={'pk': self.instance.id})

    def get_context_data(self):
        ctx = super(CustomModelForm, self).get_context_data()
        ctx['model_name'] = _(self._meta.model._meta.model_name.title())
        return ctx

    def __init__(self, *args, **kwargs):
        super(CustomModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = self.build_layout()
        self.helper.add_input(Submit('submit', 'Salvar'))
        if self.instance.id:
            self.helper.add_input(Button('delete', 'Deletar', css_class='btn-danger',
                                  onclick=f"window.location.href = '{self.get_delete_url()}'"))
        self.helper.add_input(Button('cancel', 'Cancelar', css_class='btn-primary',
                                     onclick=f"window.location.href = '{self.get_reverse_url()}'"))

    def build_layout(self):
        return {}