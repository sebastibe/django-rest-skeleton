# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.http import HttpResponse

from rest_framework.urlpatterns import format_suffix_patterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',  # noqa
    # Examples:
    url(r'^$', 'api.views.api_root', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'', include('api.users.urls')),

    # swagger doc
    url(r'^api-docs/', include('rest_framework_swagger.urls')),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html', 'xml'])

# Default login/logout views
urlpatterns += patterns('rest_framework',  # noqa
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth-token/', 'authtoken.views.obtain_auth_token', name='auth-token'),
    # url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),
)

# Disallow robots to crawl the doc
urlpatterns += patterns('',  # noqa
    url(r'^robots\.txt$',
        lambda r: HttpResponse("User-agent: *\nDisallow: /",
                               mimetype="text/plain")),
)
