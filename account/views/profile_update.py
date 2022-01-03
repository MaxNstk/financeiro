from django.urls import reverse_lazy

from account.forms import RegisterForm
from account.models import User
from finances.views.generic.custom_update_view import CustomUpdateView


class ProfileUpdateView(CustomUpdateView):
    model = User
    form_class = RegisterForm
    template_name = 'generic/generic_form.html'
    success_url = reverse_lazy('home')