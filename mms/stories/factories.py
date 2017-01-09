from django.test import TestCase
import factory
import factory.fuzzy
import geojson
import json
from . import models
from .models import StoryUser
from .models import Story
from .models import Waypoint
from .models import Submission
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.test import Client
from django.contrib.auth.models import User



class StoryUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StoryUser
    username = factory.fuzzy.FuzzyText(length=12, prefix='')
    email = factory.LazyAttribute(lambda a: u'{0}@example.com'.format(a.username).lower())
    #story = factory.RelatedFactory(StoryFactory)
    User.objects.create_user(self.username, self.email, factory.fuzzy.FuzzyText(length=12, prefix=''))

    #user = factory.SubFactory(StoryUserFactory)

class StoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Story
    name= factory.fuzzy.FuzzyText(length=8, prefix='')
    description= factory.fuzzy.FuzzyText(length=250, prefix='')
    instructions= factory.fuzzy.FuzzyText(length=350, prefix='')
    #owner= StoryUserFactory.create()

    @factory.post_generation
    def create_submissions(self, create, extracted, **kwargs):
        self.owner = StoryUserFactory.create()
        if not create:
            return
        for i in range(10):
            submission = SubmissionFactory.create(story=self)


class SubmissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Submission
    user = factory.SubFactory(StoryUserFactory)
    story = factory.SubFactory(StoryFactory)

class WaypointFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Waypoint
    waypoint = geojson.utils.generate_random("Point")
    geom = geojson.utils.generate_random("Point")
    lng = waypoint.coordinates[0]
    lat = waypoint.coordinates[1]
    notes = factory.fuzzy.FuzzyText(length=8, prefix='')
    path_order = factory.fuzzy.FuzzyInteger(0, 6)
    submission = factory.RelatedFactory(SubmissionFactory)
