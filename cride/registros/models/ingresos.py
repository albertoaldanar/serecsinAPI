
#Django
from django.db import models

#Utilities
from cride.utils.models import SerecsinModel

class Ingreso(SerecsinModel):

  cliente = models.CharField(max_length = 30, null= True, blank= True)
  mes = models.PositiveIntegerField(default = 0)
  año = models.PositiveIntegerField(default = 2019)
  importe = models.PositiveIntegerField(default = 0)
  adeudo_mes = models.PositiveIntegerField(default = 0)
  importante = models.BooleanField(default = False)
  adeudo_acumulado = models.PositiveIntegerField(default = 0)
  lugar = models.CharField(max_length = 30, null= True, blank= True)
  
  def __str__(self):
    return self.cliente
