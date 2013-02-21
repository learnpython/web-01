from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from filebrowser.sites import site

from zo.views import rebuild_index


admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('bookmarks.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/rebuild-index', rebuild_index, name='rebuild_index'),
    (r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^search/', include('haystack.urls')),
)


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
