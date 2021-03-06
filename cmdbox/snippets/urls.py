from django.conf.urls import url

from cmdbox.snippets import views


urlpatterns = [
    url(r'^$', views.snippets, name='list'),
    url(r'^(?P<slug>[^/]+)/$', views.details, name='details'),
    url(r'^(?P<slug>[^/]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<slug>[^/]+)/delete/$', views.delete, name='delete'),
]
