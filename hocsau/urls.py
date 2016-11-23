# -*- coding: utf-8 -*-
from django.conf.urls import url
from . views import *


urlpatterns = [
    url(r'^$', MyFormView.as_view(), name='index'),
    url(r'^(?P<category_slug>[-\w]+)/$', CategoryView.as_view(), name='category'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<post_slug>[-\w]+)$', PostDetails.as_view(), name='post_details'),
]