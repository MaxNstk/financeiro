from django.shortcuts import redirect
from django.views.generic import DeleteView


class CustomDeleteView(DeleteView):

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.model.objects.get(id=kwargs['pk']).user != request.user:
                return redirect('home')
            else:
                if request.method == 'GET':
                    return super(CustomDeleteView, self).get(self, request, *args, **kwargs)
                else:
                    return super(CustomDeleteView, self).post(self, request, *args, **kwargs)
        except:
            return redirect('home')
