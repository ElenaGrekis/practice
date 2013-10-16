from django.conf.urls import patterns, include, url
from library.views import index
from library.views import show

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mylib.views.home', name='home'),
    # url(r'^mylib/', include('mylib.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^library/$', index),
    url(r'^library/books/$', index),
    url(r'^books/(?P<book>\d+)/$', show, name='show')
)
