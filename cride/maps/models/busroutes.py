#Django
from django.db import models

#Utilities
from cride.utils.models import SerecsinModel

class Busroute(SerecsinModel):

  bus = models.CharField(max_length = 30, unique = False)
  helper = models.CharField(max_length = 30, unique = False)
  helper_b = models.CharField(max_length = 30, unique = False, null = True)
  gas = models.CharField(max_length = 10, unique = False)
  km = models.PositiveIntegerField(default = 0)

  start = models.DateTimeField(
    "event_date",
    help_text = "Date and time of stop"
  )
  finish = models.DateTimeField(
    "event_date",
    help_text = "Date and time of stop"
  )

  def __str__(self):
    return self.bus
