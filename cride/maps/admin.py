"""Admin for matches app"""

#django
from django.db import models
from django.contrib import admin
#model
from cride.maps.models import Busroute, Stop

@admin.register(Busroute)
class BusrouteAdmin(admin.ModelAdmin):
  list_display= (
    "start",
    "finish",
    "bus",
    "helper",
    "gas",
    "km"
  )

  search_fields = ("bus",)
  list_filter = (
   "bus",
  )

@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
  list_display= (
    "client",
    "arrived_at",
    "finished_at",
    "comments",
  )

  search_fields = ("client",)
  list_filter = (
   "client",
  )
