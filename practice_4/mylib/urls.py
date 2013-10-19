from django.conf.urls import patterns, include, url
from library.views import index
from library.views import show_book
from library.views import show_author
from library.views import list_authors

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'mylib.views.home', name='home'),
    # url(r'^mylib/', include('mylib.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^library/$', index),
    url(r'^library/books/$', index),
    url(r'^library/books/(?P<book_id>\d+)/$', show_book, name='show_book'),
    url(r'^library/authors/$', list_authors),
    url(r'^library/authors/(?P<author_id>\d+)/$', show_author, name='show_author')
)
