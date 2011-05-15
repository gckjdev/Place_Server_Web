from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^photo/', include('place.photo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
 )
