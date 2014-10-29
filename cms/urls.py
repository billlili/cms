from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/index/$','blog.views.index'),
    url(r'^poll/',include('poll.urls')),
    url(r'',include('django.contrib.flatpages.urls')),
)
