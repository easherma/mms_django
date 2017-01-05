from django.contrib.auth.models import User
from stories.models import Story, StoryUser, Submission, Waypoint
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

class StoryViewSet(viewsets.ModelViewSet):

    queryset = Story.objects.all()
    serializer_class = StorySerializer

    @detail_route()
    def waypoints(self, request, pk=None):
        #serializer = WaypointSerializer
        story = self.get_object()
        submissions = story.submissions.all()
        waypoints = []
        for submission in submissions:
            waypoint = submission.waypoints.values()
            waypoints.append(waypoint)


        # waypoints ={}
        # for submission in submissions:
        #     get submission.waypoint
        #     append
        #stories = Story.objects.prefetch_related('submission_set').all()
        #story.submission_set.all()[0].waypoint_set.all().values()

        #queryset = Story.objects.filter(id=story.id).select_related('submission_set')
        #queryset = self.get_object()
        return Response(waypoints)

    @detail_route()
    def users(self, request, pk=None):
        story = self.get_object()
        pk = self.kwargs['pk']
        queryset = StoryUser.objects.filter(submission=story.pk)
        #get to
        return Response(queryset.values())


    # def get_queryset(self):
    #     """
    #     This view should return a list of all the purchases for
    #     the user as determined by the username portion of the URL.
    #     """
    #     name = self.kwargs['name']
    #     return Story.objects.filter(name=name)

# class StoryListViewSet(viewsets.ModelViewSet):
#     """
#     See existing stories, add one
#     """
#     queryset = Story.objects.all()
#     serializer_class = StorySerializer
#     renderer_classes = (TemplateHTMLRenderer,)
#     template_name = 'rest_framework/stories_list.html'

class WaypointsByStory(viewsets.ModelViewSet):
    serializer_class = WaypointSerializer
    storyname = 'My First Story'
    queryset = Waypoint.objects.filter(submission__story__name='My First Story').select_related('submission')

#these are pretty much useless
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