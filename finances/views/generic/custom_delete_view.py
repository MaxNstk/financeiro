from django.shortcuts import redirect
from django.views.generic import DeleteView


class CustomDeleteView(DeleteView):

    def get(self, request, *args, **kwargs):
        if self.model.objects.get(id=kwargs['pk']).user != request.user:
            return redirect('home')
        else:
            return super(CustomDeleteView, self).get(self, request, *args, **kwargs)
