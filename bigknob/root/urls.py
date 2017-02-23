from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^push/$', views.push, name='push'),
    url(r'^status/$', views.status, name='status'),
]
