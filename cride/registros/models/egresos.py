#Django
from django.db import models
import datetime
#Utilities
from cride.utils.models import SerecsinModel

class Egreso(SerecsinModel):

  fecha = models.DateField(default= datetime.date.today)
  importe = models.PositiveIntegerField(default = 0)

  mes = models.PositiveIntegerField(default = 0)
  año = models.PositiveIntegerField(default = 2019)

  cliente = models.CharField(max_length = 30, null= True, blank= True)
  concepto = models.CharField(max_length = 30, null= True, blank= True)
  genero = models.CharField(max_length = 30,  null= True, blank= True)
  cantidad = models.FloatField(null=True, blank=True, default=None)
  usuario = models.CharField(max_length = 30, null= True, blank= True)
  lugar = models.CharField(max_length = 30, null= True, blank= True)

  cuenta_origen = models.PositiveIntegerField(default = 0, null = True)
  metodo_pago= models.CharField(max_length = 30, null= True, blank= True)
  forma_pago= models.CharField(max_length = 30, null= True, blank= True)

  cfdi = models.CharField(max_length = 30, null= True, blank= True)
  folio = models.CharField(max_length = 30, null= True, blank= True)

  def __str__(self):
    return self.genero
