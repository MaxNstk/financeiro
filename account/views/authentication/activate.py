from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

from account.models import User
from account.tokens.activation_token import activation_token


def activate_account(request, uidb64, token):
    
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        print(e)

    if user is not None and activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account/activation_invalid.html')