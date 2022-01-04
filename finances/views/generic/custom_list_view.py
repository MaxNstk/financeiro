from django.views.generic import ListView


class CustomListView(ListView):
    breadcrumbs = None

    def get_context_data(self, **kwargs):
        ctx = super(CustomListView, self).get_context_data()
        ctx['breadcrumbs'] = self.breadcrumbs
        return ctx

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)