"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.maps.models import Busroute
#Django
from django.db import models

#Serializer
class BusrouteModelSerializer(serializers.ModelSerializer):

  class Meta:
    """Meta class"""
    model = Busroute
    fields= (
      "id", "bus", "helper", "helper_b",
      "km", "gas", "start", "finish"
    )
