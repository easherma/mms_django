#from django.contrib.auth.models import User
from stories.models import Story, User, Waypoint
from stories.serializers import StorySerializer, UserSerializer,WaypointSerializer
from rest_framework import viewsets

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
