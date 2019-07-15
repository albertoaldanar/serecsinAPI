from django.db import models

class SerecsinModel(models.Model):

  created = models.DateTimeField(
    "created_a",
    auto_now_add = True,
    help_text = "Date time for created instance"
  )
  modified = models.DateTimeField(
    "modified_at",
    auto_now = True,
    help_text = "Date time for modified instance"
  )

  class Meta:
    abstract = True
    get_latest_by = ["created"]
    ordering = ["-created", "-modified"]
