from django.test import TestCase
import factory
import factory.fuzzy
import geojson
import json
from . import models
from .models import Story
from .models import Waypoint
from .models import Submission
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.test import Client
from django.contrib.auth.models import User

#TODO use the factory faker for attributes like so
"""
class RandomUserFactory(factory.Factory):
    class Meta:
        model = models.User

    first_name = factory.Faker('first_name')

user = RandomUserFactory()

print user.first_name"""


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.fuzzy.FuzzyText(length=12, prefix='')
    email = factory.LazyAttribute(lambda a: u'{0}@example.com'.format(a.username).lower())


class StoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Story
    name= factory.fuzzy.FuzzyText(length=8, prefix='')
    description= factory.fuzzy.FuzzyText(length=250, prefix='')
    instructions= factory.fuzzy.FuzzyText(length=350, prefix='')
    owner= factory.SubFactory(UserFactory)


class SubmissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Submission
    user = factory.SubFactory(UserFactory)
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
