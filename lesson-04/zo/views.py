from django.contrib.flatpages.models import FlatPage
from django.shortcuts import get_object_or_404

from annoying.decorators import render_to

from users.forms import RegisterForm
from users.models import UserProfile


@render_to('index.html')
def index(request):
    """
    Main page.
    """
    user = request.user

    if user.is_authenticated():
        if user.get_profile().company:
            url = '/company-{}/'.format(user.get_profile().company)
            page = get_object_or_404(FlatPage, url=url)
            context = {'company_page': page}
        else:
            companies = UserProfile.objects.exclude(company=None)
            page = get_object_or_404(FlatPage, url='/')
            context = {'companies': companies, 'page': page}
    else:
        page = get_object_or_404(FlatPage, url='/')
        context = {'form': RegisterForm(), 'page': page}

    return context
