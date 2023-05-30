from django.contrib import admin
from django.urls import path,include,re_path

from django.conf import settings
from django.conf.urls.static import serve
from django.conf.urls.i18n import i18n_patterns



urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('',include('shingle.urls')),
    path('',include('file_storge.urls')),
]
