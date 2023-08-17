from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("core.urls")),
    path("admin/", admin.site.urls, name="admin"),
    path("accounts/", include("django.contrib.auth.urls")),
]
