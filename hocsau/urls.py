# -*- coding: utf-8 -*-
from django.conf.urls import url
from . views import *


urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^(?P<category_slug>[a-zA-Z1-9\-_\/]+)/$', CategoryView.as_view(), name='category'),
    url(r'^(?P<category_slug>[a-zA-Z1-9\-_\/]+)/(?P<post_slug>[-\w]+)$', PostDetails.as_view(), name='post_details'),
]