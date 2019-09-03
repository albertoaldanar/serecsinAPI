"""Users urls"""
from django.urls import path, include
#Views
#DRF
from rest_framework.routers import DefaultRouter

from cride.registros.views import serecsin_data

router  = DefaultRouter()

urlpatterns = [
  path("serecsin_data/", serecsin_data),
  path("", include(router.urls)),
]
