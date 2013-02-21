from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from grappelli.dashboard import Dashboard, modules


class AdminDashboard(Dashboard):
    """
    Custom index dashboard for Zapis Online admin site.
    """
    def init_with_context(self, context):
        self.children.append(modules.Group(
            _('Applications'),
            column=1,
            collapsible=True,
            children=[
                modules.AppList(
                    _('Django Applications'),
                    column=1,
                    collapsible=False,
                    models=('django.contrib.*',),
                ),
                modules.AppList(
                    _('Other Applications'),
                    column=1,
                    collapsible=False,
                    exclude=('django.contrib.*',),
                )
            ]
        ))

        self.children.append(modules.LinkList(
            _('Zapis Online module'),
            column=2,
            children=[
                {
                    'title': _('Rebuild index'),
                    'url': reverse('rebuild_index'),
                    'external': False,
                },
            ]
        ))

        self.children.append(modules.LinkList(
            _('Media Management'),
            column=2,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))

        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=10,
            collapsible=False,
            column=3,
        ))
