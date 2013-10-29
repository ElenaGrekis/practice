from django.conf.urls import patterns, url

from library import views

urlpatterns = patterns('',
   # url(r'^books/$', views.index, name='index'),
   # url(r'^books/(?P<book>)/$', views.show, name='show')
   url(r'^(?P<book>)/$', views.show, name='show')
   #    url(r'^$', views.index, name='index')
)
