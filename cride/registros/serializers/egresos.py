"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.registros.models import Egreso
#Django
from django.db import models

#Serializer
class EgresoModelSerializer(serializers.ModelSerializer):

  class Meta:

    model = Egreso

    fields= (
      "fecha", "importe", "mes", "año", "concepto",
      "genero", "cantidad", "usuario", "lugar", "cuenta_origen", 
      "metodo_pago", "forma_pago", "cfdi", "folio"
    )
