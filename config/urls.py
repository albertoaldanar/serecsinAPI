"""Main URLs module."""

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path("", include(("cride.users.urls", "users"), namespace = "users")),
    path("", include(("cride.maps.urls", "maps"), namespace = "maps")),
    path("", include(("cride.registros.urls", "registros"), namespace ="registros")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
