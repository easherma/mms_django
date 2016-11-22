from stories.models import Waypoint
from stories.serializers import WaypointSerializer
from rest_framework import generics

class WaypointList(generics.ListCreateAPIView):
    queryset = Waypoint.objects.all()
    serializer_class = WaypointSerializer

class WaypointDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Waypoint.objects.all()
    serializer_class = WaypointSerializer
