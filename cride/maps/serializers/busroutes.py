"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.maps.models import Busroute
#Django
from django.db import models
from cride.users.serializers import UserModelSerializer

#Serializer
class BusrouteModelSerializer(serializers.ModelSerializer):

  class Meta:
    company = UserModelSerializer(read_only = True)

    model = Busroute
    fields= (
      "company", "id", "bus", "helper", "helper_b",
      "km", "gas", "start", "finish"
    )
