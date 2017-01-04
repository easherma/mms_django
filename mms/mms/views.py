from django.views.generic.base import TemplateView
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
from django.shortcuts import render


class HomePageView(TemplateView):

    template_name = "index.html"
    title = "List of Stories"

    def stories(self):
        return Story.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super(HomePageView, self).get_context_data(**kwargs)
    #     context['latest_articles'] = Story.objects.all()
    #     return context
