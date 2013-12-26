from django.conf.urls import patterns, url

from guidepocapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<region_id>\d+)/$', views.detail_region, name='region details'),
    url(r'^(?P<region_id>\d+)/(?P<place_id>\d+)/$', views.detail_place, name='place details'),
    url(r'^guides/(?P<guide_id>\d+)/$', views.detail_guide, name='guide details'),
    url(r'^guides/register/$', views.register_guide, name='register guide'),
    url(r'^guides/register/complete/$', views.complete, name='register complete'),
)