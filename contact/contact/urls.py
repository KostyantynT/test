from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login

from views import ContactView
from views import ContactUpdate
from views import RequestsView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ContactView.as_view(), name='contact_view'),
 
    url(r'^edit/(?P<pk>\d+)/$', login_required(ContactUpdate.as_view()), name='contact_edit'),
    url(r'^middleware/$', RequestsView.as_view(), name='requests_view'),
    url(r'^login$', login, name='login'),
    url(r'^login(?P<next>.*)$', login, {'next': '/'}, name='login_next'),
    # url(r'^contact/', include('contact.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
