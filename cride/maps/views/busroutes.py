from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import action
#Serializers
from cride.maps.serializers import BusrouteModelSerializer
#models
from cride.maps.models import Busroute

class BusroutesViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet,
                    APIView):
  """Request view set"""

  serializer_class = BusrouteModelSerializer
  queryset = Busroute.objects.all()


@api_view(["POST"])
def post_busroute(request):
      response = Busroute.objects.create(
        bus = request.data["bus"],
        helper = request.data["helper"],
        helper_b = request.data["helper_b"],
        gas = request.data["gas"],
        km = request.data["km"],
        start = request.data["start"],
        finish = request.data["start"]
      )

      data = {"busroute": BusrouteModelSerializer(response).data}

      return Response(data)
