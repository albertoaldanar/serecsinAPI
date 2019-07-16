#Django
from django.db import models

#Utilities
from cride.utils.models import SerecsinModel

class Stop(SerecsinModel):

  lng = models.FloatField(blank=True)
  lat = models.FloatField(blank=True)

  busroute = models.ForeignKey(
    "maps.Busroute",
    related_name = "busroute",
    on_delete = models.CASCADE
  )

  client = models.CharField(max_length = 30, unique = False, null = True)
  comments = models.CharField(max_length = 40, null = True)
  km = models.PositiveIntegerField(default = 0)

  arrived_at = models.DateTimeField(
    "event_date",
    help_text = "Date and time of stop"
  )

  finished_at = models.DateTimeField(
    "event_date",
    help_text = "Date and time of stop"
  )


  def __str__(self):
    return self.client
