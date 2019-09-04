"""Events API views"""
#DRF
from rest_framework.views import APIView
from rest_framework import status, mixins, viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import generics
from operator import itemgetter, attrgetter
import csv 
import io

#Django
from django.db.models import Q, Sum, Count
from django.db.models.functions import Extract
#Serializer
from cride.registros.serializers import EgresoModelSerializer, IngresoModelSerializer
from cride.maps.serializers import StopModelSerializer
#Utilities
from heapq import nlargest
#Models
from cride.registros.models import Ingreso, Egreso
from cride.maps.models import Busroute, Stop

# class RegistrosViewSet(mixins.CreateModelMixin,
#                     mixins.ListModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     viewsets.GenericViewSet):


@api_view(["GET"])
def serecsin_data(request):
  current_month = request.query_params.get("month")
  current_year = request.query_params.get("year")	

  total_ingresos = Ingreso.objects.filter(mes = current_month, año = current_year).aggregate(Sum("importe"))
  # total_ingresos = Ingreso.objects.aggregate(Sum("importe"))

  total_egresos = Egreso.objects.filter(mes = current_month, año = current_year).aggregate(Sum("importe"));

  ingreso_by_month = Ingreso.objects.values('mes').annotate(Sum('importe')).order_by('mes')
  egreso_by_month = Egreso.objects.values('mes').annotate(Sum('importe')).order_by('mes')


  e_m = Egreso.objects.filter(mes = current_month, año = current_year, lugar = "Mochis")
  egreso_mochis = e_m.values("genero").annotate(Sum("importe")).order_by("genero")


  e_c = Egreso.objects.filter(mes = current_month , año = current_year,  lugar = "Culiacan")
  egreso_cln = e_c.values("genero").annotate(Sum("importe")).order_by("genero")

  e_q = Egreso.objects.filter(mes = current_month, año = current_year, lugar = "Queretaro")
  egreso_qro = e_q.values("genero").annotate(Sum("importe")).order_by("genero")


  #Stops
  month_stops= Stop.objects.filter(busroute__mes = current_month, busroute__year= current_year)
  stops = month_stops.values("client").annotate(Count('client')).order_by("client")

  #Utilidad por cliente
  utils = Ingreso.objects.filter(mes = current_month, año = current_year)
  pay_by_client = utils.values("cliente").annotate(Sum("importe")).order_by("cliente")


  total_rec = Stop.objects.filter( ~Q(client = "BASURA"), fail = False, busroute__mes = current_month, busroute__year= current_year).count()
  total_rec_fail = Stop.objects.filter(fail = True, busroute__mes = current_month, busroute__year= current_year).count()
  descargas = Stop.objects.filter(fail = False, busroute__mes = current_month, client = "BASURA", busroute__year= current_year).count()
  incidentes = Stop.objects.filter(busroute__mes = current_month, client = "INCIDENTE", busroute__year= current_year).count()



  #Ingresos por grupo 
  bonatti = Ingreso.objects.filter(mes = current_month, año = current_year, cliente = "Bonatti")
  total_bonatti = bonatti.aggregate(Sum('importe'))

  oxxo = Ingreso.objects.filter(mes = current_month, año = current_year, cliente = "Oxxo")
  total_oxxo = oxxo.aggregate(Sum('importe'))

  tiendas = Ingreso.objects.filter(~Q(Q(cliente = "Bonatti") | Q(cliente = "Oxxo")), mes = current_month, año = current_year)
  total_tiendas = tiendas.aggregate(Sum('importe'))



  #Gastos por grupo
  bonatti_gastos = Stop.objects.filter(busroute__mes = current_month, busroute__year = current_year, client = "Bonatti").count()
  oxxo_gastos = Stop.objects.filter(busroute__mes = current_month, busroute__year = current_year, client = "Oxxo").count()
  tiendas_gastos = Stop.objects.filter(~Q(Q(client = "Bonatti") | Q(client = "Oxxo")), busroute__mes = current_month, busroute__year = current_year).count()

  # mochis = Ingreso.objects.filter(mes = current_month, año = current_year, lugar = "Mochis")
  # total_mochis = mochis.aggregate(Sum('importe'))

  calendar = Stop.objects.filter(busroute__mes = current_month, busroute__year = current_year)

  data = {
       	"total_egresos": total_egresos,
        "total_ingresos": total_ingresos,
        "ingreso_by_month": ingreso_by_month,
        "egreso_by_month": egreso_by_month,
        "egreso_cln": egreso_cln,
        "egreso_qro": egreso_qro,
        "egreso_mochis": egreso_mochis,
        "stops_by_client": stops, 
        "pay_by_client": pay_by_client, 
        "total_rec": total_rec,
        "total_rec_fail": total_rec_fail,
        "descargas": descargas,
        "incidentes": incidentes, 
        "calendar": StopModelSerializer(calendar, many = True).data, 
        "bonatti": total_bonatti["importe__sum"], 
        "oxxo": total_oxxo["importe__sum"], 
        "gastos_bonatti": bonatti_gastos, 
        "gastos_oxxo": oxxo_gastos, 
        "gastos_tiendas": tiendas_gastos, 
        "total_tiendas": total_tiendas["importe__sum"]
  }
 

  return Response(data)