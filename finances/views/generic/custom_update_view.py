from django.utils.translation import gettext as _
from django.views.generic import UpdateView


class CustomUpdateView(UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(CustomUpdateView, self).get_context_data()
        ctx['model_name'] = _(self.form_class._meta.model._meta.object_name)
        return ctx