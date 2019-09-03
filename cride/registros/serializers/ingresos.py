"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.registros.models import Ingreso
#Django
from django.db import models

#Serializer
class IngresoModelSerializer(serializers.ModelSerializer):

  class Meta:

    model = Ingreso

    fields= (
  	  "importe", "mes", "año",
      "adeudo_mes", "importante", "adeudo_acumulado"
    )
