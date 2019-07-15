"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.maps.models import Stop
#Django
from django.db import models
#serializers
from cride.maps.serializers import BusrouteModelSerializer

#Serializer
class StopModelSerializer(serializers.ModelSerializer):
  busroute = BusrouteModelSerializer(read_only = True)

  class Meta:
    """Meta class"""
    model = Stop
    fields= (
      "id", "lat", "lng", "client",
      "comments", "busroute", "arrived_at", "finished_at"
    )
