"""Users urls"""
from django.urls import path, include
#Views
from .views import busroutes as busroutes_views
from .views import stops as stops_views
from cride.maps.views import post_busroute, post_stop
#DRF
from rest_framework.routers import DefaultRouter

router  = DefaultRouter()
router.register(r"busroutes", busroutes_views.BusroutesViewSet, basename = "busroutes")
router.register(r"stops", stops_views.StopsViewSet, basename = "stops")

urlpatterns = [
  path("", include(router.urls)),
  path("post_busroute/", post_busroute),
  path("post_stop/", post_stop),

]
