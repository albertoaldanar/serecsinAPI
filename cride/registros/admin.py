
#django
from django.db import models
from django.contrib import admin
#model
from cride.registros.models import Egreso, Ingreso

@admin.register(Ingreso)
class IngresosAdmin(admin.ModelAdmin):
  list_display= (
    "cliente", "importe", "adeudo_mes", "adeudo_acumulado"
  )

  search_fields = ("cliente",)
  list_filter = (
   "cliente", 
  )

@admin.register(Egreso)
class EgresosAdmin(admin.ModelAdmin):
  list_display= (
    "fecha", "importe", "cliente", "concepto", "genero"
  )

  search_fields = ("cliente",)
  list_filter = (
   "cliente", 
  )
