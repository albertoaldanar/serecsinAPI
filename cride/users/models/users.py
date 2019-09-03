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

  phone_number = models.CharField(max_length = 17, blank = True, null= True)

  USERNAME_FIELD = "username"

  def __str__(self):
    return self.username

  def get_short_name(self):
    return self.username
