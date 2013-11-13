from django.conf.urls import patterns, url

from library import views

urlpatterns = patterns(
    '',
    url(r'^(?P<book_id>)/$', views.show, name='show')
)
