from django.conf.urls import patterns, include, url

from library.views import BookListView, AuthorListView, BookDetailView, AuthorDetailView

from django.contrib.auth.views import login, logout
from django.contrib.auth.forms import AuthenticationForm
from library.views import register


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'mylib.views.home', name='home'),
    # url(r'^mylib/', include('mylib.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^register/$', register),
    url(r'^library/$', BookListView.as_view()),
    url(r'^library/books/$', BookListView.as_view()),
    url(r'^library/books/(?P<pk>\d+)/$', BookDetailView.as_view(), name='show_book'),
    url(r'^library/authors/$', AuthorListView.as_view()),
    url(r'^library/authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='show_author')
)
