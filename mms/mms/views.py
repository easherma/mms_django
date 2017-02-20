from django.views.generic.base import TemplateView
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
from django.shortcuts import render
import random



class HomePageView(TemplateView):


    template_name = "index.html"
    title = "Stories"


    def stories(self):
        random_idx = random.randint(0, Story.objects.count() - 1)
        random_story= Story.objects.all()[random_idx]
        return random_story

    def users(self):
        return User.objects.all()

    def submissions(self):
        return submissions.objects.all()

    def waypoints(self):
        return Waypoint.objects.all()

class StoryPageView(TemplateView):

    template_name = "index.html"
    title = "Stories"

    def stories(self, **kwargs):
        story = Story.objects.get(id=kwargs['story_id'])

        return story

    def users(self):
        return StoryUser.objects.all()

    def submissions(self):
        return submissions.objects.all()

    def waypoints(self):
        return Waypoint.objects.all()



# class StoryPageView(generics.RetrieveAPIView):
#     #queryset = Story.objects.all()
#     serializer_class = StorySerializer
#     template_name = "index.html"
#     renderer_classes = (TemplateHTMLRenderer,)
#     def get_queryset(self):
#         id = self.kwargs['pk']
#         title = "Stories"
#         return Story.objects.filter(pk=id).select_related('user')
#     def users(self):
#         return User.objects.all()
#



#Entry.objects.select_related().filter(blog=b).update(headline='Everything is the same')
        #create story
        #users in story
        #waypoints for each user (submissions?)
        #query object, parse into geojson
        #make a route that prints the geojson

    # def get_context_data(self, **kwargs):
    #     context = super(HomePageView, self).get_context_data(**kwargs)
    #     context['latest_articles'] = Story.objects.all()
    #     return context

# class StoryView(APIView):
#     """
#     A view that returns the count of active users in JSON.
#     """
#     renderer_classes = (JSONRenderer, )
#
#     def get(self, request, format=None):
#         user = User.objects.all()
#         story = Story.objects.all()
#         content = {'user_count': user_count}
#         return Response(content)
