from django.contrib.admin.views.decorators import staff_member_required
from django.core.management import call_command
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


@staff_member_required
def rebuild_index(request):
    """
    Call rebuild index custom management command from admin panel.
    """
    call_command('rebuild_index', interactive=False)
    return redirect(request.META.get('HTTP_REFERER', reverse('admin:index')))
