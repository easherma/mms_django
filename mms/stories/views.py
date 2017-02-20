from django.contrib.auth.models import User
from stories.models import Story, Submission, Waypoint
from stories.serializers import StorySerializer, UserSerializer, SubmissionSerializer, WaypointSerializer
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import detail_route, list_route
from rest_framework.renderers import JSONRenderer
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
import geojson
import json

def waypoint_to_geojson(waypoint, properties):
    geometry= waypoint['geom']

    #[f.name for f in models.Waypoint._meta.get_fields()]
    feature = geojson.Feature(geometry=geometry, properties=properties)
    return feature

class StoryViewSet(viewsets.ModelViewSet):

    queryset = Story.objects.all()
    serializer_class = StorySerializer

    @detail_route()
    def waypoints(self, request, pk=None):
        #serializer = WaypointSerializer
        story = self.get_object()
        submissions = story.submissions.all()
        #waypoints = []
        for submission in submissions:
            #waypoints = submission.waypoints
            features = []
            for waypoint in submission.waypoints.values():
                geom = geojson.loads(waypoint['geom'])
                #should return just the props we need
                properties = waypoint
                #geom['properties'] = properties
                feature = geojson.Feature(geometry=geom, properties=properties)
                features.append(feature)
            waypoints = geojson.FeatureCollection(features)
        return Response(waypoints)

    @detail_route()
    def users(self, request, pk=None):
        story = self.get_object()
        pk = self.kwargs['pk']
        queryset = User.objects.filter(submission=story.pk)
        #get to
        return Response(queryset.values())


class WaypointsByStory(viewsets.ModelViewSet):
    serializer_class = WaypointSerializer
    storyname = 'My First Story'
    queryset = Waypoint.objects.filter(submission__story__name='My First Story').select_related('submission')

#these are pretty much useless
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
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
