#Django
from django.db import models
import datetime
#Utilities
from cride.utils.models import SerecsinModel

class Busroute(SerecsinModel):

  company = models.ForeignKey(
    "users.User",
    related_name = "user",
    on_delete = models.CASCADE,
    null = True
  )

  year = models.PositiveIntegerField(default = 0)

  bus = models.CharField(max_length = 30, unique = False)
  helper = models.CharField(max_length = 30, unique = False)
  helper_b = models.CharField(max_length = 30, unique = False, null = True)
  gas = models.CharField(max_length = 20, unique = False)
  km = models.PositiveIntegerField(default = 0)

  mes = models.PositiveIntegerField(default = 0)

  is_finished = models.BooleanField(default = False)

  start = models.DateTimeField(
    "event_date",
    help_text = "Date and time of stop"
  )

  finish = models.DateTimeField(
    "event_date",
    help_text = "Date and time of stop",
    null = True
  )

  def __str__(self):
    return self.bus
