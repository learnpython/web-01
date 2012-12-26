from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'zo.views.index', name='index'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls')),
)


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
