from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static


from .views import ContactView
from settings import STATIC_ROOT

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ContactView.as_view(), name='contact_view'),
    # url(r'^contact/', include('contact.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': STATIC_ROOT},
))
