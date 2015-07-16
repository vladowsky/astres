from django.conf.urls import patterns, url, include
from ditresa import views

urlpatterns = patterns('',
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'register/$', views.register, name='register'),
    # ex: /astro/index/
    url(r'^index/$', views.index, name='index'),
    # ex: /astro/howto/
    url(r'howto/$', views.howto, name='howto'),
    # ex: /astro/
    url(r'^$', views.aslist, name='aslist'),
    # ex: /astro/5/
    url(r'^(?P<natal_id>\d+)/$', views.detail, name='detail'),
    # ex: /astro/5/edit
    url(r'^(?P<natal_id>\d+)/edit/$', views.edit, name='edit'),
    # ex: /astro/5/delete
    url(r'^(?P<natal_id>\d+)/delete/$', views.delete, name='delete'),
    # ex: /astro/5/graph/0
    url(r'^(?P<natal_id>\d+)/graph/(?P<esolevel>\d+)/$', views.graph, 
        name='graph'),
    # ex: /astro/new/
    url(r'^new/$', views.new, name='new'),

)

