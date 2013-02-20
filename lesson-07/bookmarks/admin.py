from django.contrib import admin
from django.core.urlresolvers import reverse
from django.template.defaultfilters import truncatechars
from django.utils.translation import ugettext_lazy as _

from .models import Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    """
    Customize bookmark admin representation.
    """
    list_display = ('uid', 'user_link', 'title', 'url', 'short_description')
    list_display_links = ('uid', 'title', 'url')
    list_filter = ('user', )
    list_select_related = True
    search_fields = ('title', 'url', 'short_description')

    def short_description(self, obj):
        """
        Print only 80 chars from bookmark description.
        """
        return truncatechars(obj.description, 80)

    short_description.admin_order_field = 'description'
    short_description.short_description = _('Short description')

    def user_link(self, obj):
        """
        Print link to edit user page.
        """
        label = obj.user.get_full_name() or obj.user.username
        url = reverse('admin:auth_user_change', args=[obj.user.pk])
        return u'<a href="{}">{}</a>'.format(url, label)

    user_link.admin_order_field = 'user'
    user_link.allow_tags = True
    user_link.short_description = _('User')


admin.site.register(Bookmark, BookmarkAdmin)
