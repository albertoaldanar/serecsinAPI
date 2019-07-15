from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import action
#Serializers
from cride.maps.serializers import StopModelSerializer
#models
from cride.maps.models import Stop, Busroute

class StopsViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet,
                    APIView):
  """Request view set"""

  serializer_class = StopModelSerializer
  queryset = Stop.objects.all()


@api_view(["POST"])
def post_stop(request):
      busroute = Busroute.objects.last()
      response = Stop.objects.create(
        lng = request.data["lng"],
        busroute = busroute,
        lat = request.data["lat"],
        client = request.data["client"],
        comments = request.data["comments"],
        arrived_at = request.data["arrived_at"],
        finished_at = request.data["finished_at"]
      )

      data = {"stop": StopModelSerializer(response).data}

      return Response(data)
