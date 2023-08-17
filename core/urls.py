from django.urls import path, include, re_path

from core.views import management

urlpatterns = [
    path("", management.index, name="index"),
    path("datenschutz", management.datenschutz, name="datenschutz"),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
]
