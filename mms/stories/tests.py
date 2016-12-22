from django.test import TestCase
import factory
import factory.fuzzy
import geojson
import json
from . import models
from .models import StoryUser
from .models import Waypoint
from .models import Submission
#from rest_framework import APIClient, APIRequestFactory

class StoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Story
    name= factory.fuzzy.FuzzyText(length=8, prefix='')
    description= factory.fuzzy.FuzzyText(length=250, prefix='')
    instructions= factory.fuzzy.FuzzyText(length=350, prefix='')

class StoryUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StoryUser
    username = factory.fuzzy.FuzzyText(length=12, prefix='')
    email = factory.LazyAttribute(lambda a: '{0}@example.com'.format(a.username).lower())


class SubmissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Submission
    user = factory.SubFactory(StoryUserFactory)
    story = factory.SubFactory(StoryFactory)

class WaypointFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Waypoint
    geom = geojson.utils.generate_random("Point")
    lng = factory.fuzzy.FuzzyDecimal(-180, 180, precision=5)
    lat = factory.fuzzy.FuzzyDecimal(-90, 90, precision=5)
    notes = factory.fuzzy.FuzzyText(length=8, prefix='')
    path_order = factory.fuzzy.FuzzyInteger(0, 6)
    submission = factory.SubFactory(SubmissionFactory)

class StoryTestCase(TestCase):
    def test_something(self):
        story = StoryFactory.create_batch(3)

class UserTestCase(TestCase):
    def test_something(self):
        user = StoryUserFactory.create_batch(5)
        users = StoryUser.objects.all()
        self.assertEqual(users.count(), 5)
        self.assertIsNotNone(users[0].id)

class WaypointTestCase(TestCase):
    def test_something(self):
        #waypoint = WaypointFactory.create_batch(5)
        waypoint = WaypointFactory.create()
        waypoints = Waypoint.objects.all()
    def test_multWaypointForSubmission(self):
        submission = SubmissionFactory.create()
        waypoint = WaypointFactory.create_batch(5, submission=submission)
        waypoints = Waypoint.objects.all()
        self.assertIsNotNone(waypoints[0].id)
        self.assertEqual(waypoints[0].submission, submission)
        self.assertEqual(waypoints.count(), 5)
        for waypoint in waypoints:
            self.assertEqual(waypoint.submission, submission)
            #print waypoint.id, submission.id, submission.user, submission.story
#let waypoint geom be blank
class SubmissionTestCase(TestCase):
    def test_something(self):
        submission = SubmissionFactory.create()
        all_entries= models.Submission.objects.all()
        #maybe test many to one relationship
    def test_submission(self):
        story = StoryFactory.create()
        user = StoryUserFactory.create()
        submission = SubmissionFactory.create(story = story, user = user)
        self.assertEqual(submission.story, story)
        self.assertEqual(submission.user, user)
        waypoint = WaypointFactory.create_batch(5, submission=submission)
        #waypoints = Waypoint.objects.all()
        submissions = Submission.objects.all()







#class OutputTestCase(TestCase):

    #def geojson(self):
        #create story
        #users in story
        #waypoints for each user (submissions?)
        #query object, parse into geojson
        #make a route that prints the geojson
