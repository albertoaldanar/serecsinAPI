#django
from django.db import models
from django.contrib.auth.models import AbstractUser
#Utilities
from cride.utils.models import SerecsinModel
from django.core.validators import RegexValidator

class User(SerecsinModel, AbstractUser):

  email = models.EmailField(
    "email addres",
    unique = True,
    error_messages = {
      "unique": "Username aleready taken"
    }
  )

  phone_number = models.CharField(max_length = 17, blank = True)

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["username", "first_name", "last_name"]

  def __str__(self):
    return self.username

  def get_short_name(self):
    return self.username
