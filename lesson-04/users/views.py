from django.contrib import auth
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

from annoying.decorators import render_to

from users.forms import LoginForm, RegisterForm


@render_to('users/login.html')
def login(request):
    """
    Login page.
    """
    if request.user.is_authenticated():
        return redirect('index')

    form = LoginForm(request.POST or None)

    if form.is_valid():
        try:
            user = form.login(request)
        except ValidationError as err:
            form._errors['__all__'] = err.messages
        else:
            return redirect('index')

    return {'form': form}


def logout(request):
    """
    Logout page.
    """
    if request.user.is_authenticated():
        auth.logout(request)
    return redirect('index')


@render_to('users/register.html')
def register(request):
    """
    Register page.
    """
    if request.user.is_authenticated():
        return redirect('index')

    form = RegisterForm(request.POST or None)

    if form.is_valid():
        try:
            user = form.register(request)
        except ValidationError as err:
            form._errors['__all__'] = err.messages
        else:
            return redirect('index')

    return {'form': form}
