from django.contrib.auth.models import User
from stories.models import Story, StoryUser, Submission, Waypoint
from stories.serializers import StorySerializer, UserSerializer, SubmissionSerializer, WaypointSerializer
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = StoryUser.objects.all()
    serializer_class = UserSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

class WaypointViewSet(viewsets.ModelViewSet):
    queryset = Waypoint.objects.all()
    serializer_class = WaypointSerializer

class StoryList(APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'stories_list.html'

    def get(self, request):
        queryset = Story.objects.all()
        return Response({'stories': queryset})
