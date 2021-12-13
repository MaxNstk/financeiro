from django.views.generic import UpdateView


class CustomUpdateView(UpdateView):
    breadcrumbs = None

    def get_context_data(self, **kwargs):
        ctx = super(CustomUpdateView, self).get_context_data()
        ctx['breadcrumbs'] = self.breadcrumbs
        return ctx
    
    def get_form_kwargs(self):
        kwargs = super(CustomUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs