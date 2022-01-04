from django.shortcuts import redirect
from django.views.generic import UpdateView


class CustomUpdateView(UpdateView):
    breadcrumbs = None

    def get_context_data(self, **kwargs):
        ctx = super(CustomUpdateView, self).get_context_data()
        ctx['breadcrumbs'] = self.breadcrumbs
        return ctx

    def get(self, request, *args, **kwargs):
        if self.model.objects.get(id=kwargs['pk']).user != request.user:
            return redirect('home')
        else:
            return super(CustomUpdateView, self).get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if self.model.objects.get(id=kwargs['pk']).user != request.user:
            return redirect('home')
        else:
            return super(CustomUpdateView, self).get(self, request, *args, **kwargs)
