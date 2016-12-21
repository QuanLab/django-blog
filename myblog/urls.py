from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hocsau/', include("hocsau.urls")),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]