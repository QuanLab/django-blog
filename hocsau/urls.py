# -*- coding: utf-8 -*-
from django.conf.urls import url
from . views import *


urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^(?P<category>[-\w]+)/$', CategoryView.as_view(), name='category'),
    url(r'^(?P<category>[-\w]+)/(?P<sub_category>[-\w]+)/$', CategoryView.as_view(), name='sub_category'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<post_slug>[a-zA-Z1-9\-_\/]+)/$',
        PostDetail.as_view(), name='post_detail'),
]