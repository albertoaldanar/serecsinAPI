"""User model admin."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from cride.users.models import User

class CustomUserAdmin(UserAdmin):
  list_display = ("email", "username", "first_name")

admin.site.register(User, CustomUserAdmin)

