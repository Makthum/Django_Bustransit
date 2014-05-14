from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bustranit.views.home', name='home'),
    # url(r'^untitled/', include('untitled.foo.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^findbus/$','bustranit.views.findbus',name='findbus'),

    url(r'^searchbus/$','bustranit.views.searchbus',name='searchbus'),

    url(r'^schedule/$','bustranit.views.schedule',name='schedule'),
    url(r'^locate/$','bustranit.views.locate',name='schedule'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
