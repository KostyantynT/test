from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from views import ContactView
from views import RequestsView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ContactView.as_view(), name='contact_view'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(ContactView.as_view()), name='contact_edit'),
    url(r'^middleware/', RequestsView.as_view(), name='requests_view'),
    
    # url(r'^contact/', include('contact.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT},
))
