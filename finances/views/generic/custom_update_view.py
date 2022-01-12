from django.shortcuts import redirect
from django.views.generic import UpdateView


class CustomUpdateView(UpdateView):
    breadcrumbs = None

    def get_context_data(self, **kwargs):
        ctx = super(CustomUpdateView, self).get_context_data()
        ctx['breadcrumbs'] = self.breadcrumbs
        return ctx

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.model.objects.get(id=kwargs['pk']).user != request.user:
                return redirect('home')
            else:
                if request.method == 'GET':
                    return super(CustomUpdateView, self).get(self, request, *args, **kwargs)
                else:
                    return super(CustomUpdateView, self).post(self, request, *args, **kwargs)
        except:
            return redirect('home')