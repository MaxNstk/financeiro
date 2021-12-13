from django.views.generic import CreateView


class CustomCreateView(CreateView):
    breadcrumbs = None

    def get_context_data(self, **kwargs):
        ctx = super(CustomCreateView, self).get_context_data()
        ctx['breadcrumbs'] = self.breadcrumbs
        return ctx

    def get_form_kwargs(self):
        kwargs = super(CustomCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
