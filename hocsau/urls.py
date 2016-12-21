# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . views import *
from django.contrib.sitemaps.views import sitemap
from hocsau.sitemap import JobPostSitemap
from django.views.decorators.cache import cache_page

sitemaps={
     'jobs': JobPostSitemap,
}

urlpatterns = [
    url(r'pages', include('django.contrib.flatpages.urls')),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^(?P<category>[-\w]+)/$', CategoryView.as_view(), name='category'),
    url(r'^(?P<category>[-\w]+)/(?P<sub_category>[-\w]+)/$', CategoryView.as_view(), name='sub_category'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<post_slug>[-\w]+)/$',
        PostDetail.as_view(), name='post_detail'),
    url(r'^sitemap\.xml$', cache_page(86400)(sitemap), {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]