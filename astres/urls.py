from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^astro/', include('ditresa.urls', namespace="astro")),
    url(r'^admin/', include(admin.site.urls)),
)


