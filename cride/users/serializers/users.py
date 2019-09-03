"""Users Seliralizers"""
#Django
from django.contrib.auth import authenticate, password_validation
from django.core.validators import RegexValidator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from django.conf import settings
#DRF
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from rest_framework import serializers
#Models
from cride.users.models import User
#utilities
from datetime import timedelta
import jwt

from django.db import models
#Serializer

class UserModelSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = (
      "username",
      "email",
      "first_name",
      "last_name",
    )

class UserSignUpSerializer(serializers.Serializer):
  """UserSignupSerializer"""
  email = serializers.EmailField(
    validators = [UniqueValidator(queryset= User.objects.all())]
  )
  username = serializers.CharField(
    min_length = 4,
    max_length = 20,
    validators = [UniqueValidator(queryset= User.objects.all())]
  )

  password = serializers.CharField(min_length=  8, max_length = 64)
  password_confirmation = serializers.CharField(min_length=  8, max_length = 64)

  def validate(self, data):
    password = data["password"]
    password_confirmation = data["password_confirmation"]

    if password != password_confirmation:
        raise serializers.ValidationError("Password doesnt match")
    password_validation.validate_password(password)
    return data

  def create(self, data):
    data.pop("password_confirmation")
    user = User.objects.create_user(**data)
    # self.send_confrimation_email(user)
    self.gen_verification_token(user)
    jwt, created = Token.objects.get_or_create(user = user)
    return user, jwt.key

  def send_confrimation_email(self, user):
    verifcation_token = self.gen_verification_token(user)
    subject = "Welcome @{}! Verify your account".format(user.username)
    from_email = "Compare ride <noreply@comparteride.com"
    content = render_to_string(
        "templates.account_verification.html",
        {"token": verifcation_token, "user": user}
    )
    msg = EmailMultiAlternatives(subject,content, from_email, [user.email])
    msg.attach_alternative(content, "text/html")
    msg.send()


  def gen_verification_token(self, user):
    """Create JWT"""
    exp_date = timezone.now() + timedelta(days = 3)
    payload = {
      "user": user.username,
      "exp": int(exp_date.timestamp()),
      "type": "email_confirmation",
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm ="HS256")
    return token.decode()

#Login user
class UserLoginSerializer(serializers.Serializer):
  """Login data"""
  username = serializers.CharField(
    min_length = 6, max_length = 20,
  )
  password = serializers.CharField(min_length =8, max_length =64)

  def validate(self, data):
      user = authenticate(username = data["username"], password = data["password"])
      if not user:
          raise serializers.ValidationError("Invalid credential")
      self.context["user"] = user
      return data

  def create(self, data):
      token, created = Token.objects.get_or_create(user = self.context["user"])
      return self.context["user"], token.key

class AccountVerificationSerializer(serializers.Serializer):
    """Account verification Serializer"""
    token = serializers.CharField()

    def validate_token(self, data):
      """Verify is valid"""
      try:
        payload = jwt.decode(data, setting.SECRET_KEY, algorithm =["HS256"])
      except jwt.ExpiredSignatureError:
          raise serializers.ValidationError("Verification link has expired.")
      except jwt.PyJWTError:
          raise serializers.ValidationError("Invalid Token")
      if payload["type"] != "email_confirmation":
          raise serializers.ValidationError("Invalid Token")

      self.context["payload"] = payload
      return data

      def save(self):
        """Update users verified status"""
        payload = self.context["payload"]
        user = User.objects.get(username = payload["user"])
        user.save()
