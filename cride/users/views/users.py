""" Users views"""
#DRF
from rest_framework.views import APIView
from rest_framework import status, mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
#Permissions
from rest_framework.permissions import (
  AllowAny,
  IsAuthenticated
)
#Serializers
from users.serializers.users import (
  UserLoginSerializer,
  UserModelSerializer,
  UserSignUpSerializer,
  AccountVerificationSerializer
)
from cride.users.models import User

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
  """User view set"""
  """Handle Login, SignUp y verification"""

  queryset = User.objects.filter(is_active = True)
  serializer_class = UserModelSerializer
  lookup_field = "username"

  def get_permissions(self):
    """Asign Permission based on action"""
    if self.action in ["signup", "login", "verify"]:
        permissions = [AllowAny]
    elif self.action == ["retrieve", "update", "partial_update"]:
        permissions = [IsAuthenticated, IsAccountOwner]
    else:
        permissions = [IsAuthenticated]
    return [p() for p in permissions]

  @action(detail=False, methods=['post'])
  def login(self, request):
      serealizer = UserLoginSerializer(data = request.data)
      serealizer.is_valid(raise_exception =True)
      user, token = serealizer.save()

      data = {
        "user": UserModelSerializer(user).data,
        "jwt": token
      }
      return Response(data, status = status.HTTP_201_CREATED)


  @action(detail=False, methods=["post"])
  def signup(self, request):
      serealizer = UserSignUpSerializer(data = request.data)
      serealizer.is_valid(raise_exception =True)
      user, jwt = serealizer.save()
      data = {
        "user": UserModelSerializer(user).data,
        "jwt": jwt
      }

      return Response(data, status = status.HTTP_201_CREATED)


  @action(detail=False, methods=["post"])
  def verify(self, request):
      serealizer = AccountVerificationSerializer(data = request.data)
      serealizer.is_valid(raise_exception =True)
      serealizer.save()

      data = {"message": "Congratulations now go to the app"}

      return Response(data, status = status.HTTP_200_OK)

  def retrieve(self, request, *args, **kwargs):
      response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
      data = {
        "user": response.data,
      }
      response.data = data
      return response

