# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from . import views
admin.autodiscover()


# urlpatterns = [
#     url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
#         {'sitemaps': {'cmspages': CMSSitemap}}),
#     # url(r'^select2/', include('django_select2.urls')),
# ]

# urlpatterns += i18n_patterns('',
# 	url(r'^admin/', include(admin.site.urls)),  # NOQA
# 	url(r'^$', views.index, name='index'),
# 	url(r'^', include('cms.urls')),
# )

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^cportal/', include('customerportal.urls')),
	url(r'^$', include('home.urls')),
	url(r'^', include('cms.urls')),
]

# This is only needed when using runserver.
# if settings.DEBUG:
#     urlpatterns = [
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#             {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#         ] + urlpatterns + staticfiles_urlpatterns()
