from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoRTAppEnv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^djangoRT/', include('djangoRT.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
)
