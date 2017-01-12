from django.test import TestCase
import factory
import factory.fuzzy
import geojson
import json
from . import models
from .models import Waypoint
from .models import Submission
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.test import Client
from django.contrib.auth.models import User
from stories import factories
from stories.factories import WaypointFactory, StoryFactory, SubmissionFactory, UserFactory

class ReadTestCase(TestCase):
    """setup db and create some inital data"""
    def setUp(self):
        """create story with random id, populate it with 5 submissions. each submission has 5 waypoints"""
        id = factory.fuzzy.FuzzyInteger(0, 256)
        self.story_id = id.fuzz()
        story = factories.StoryFactory.create(id=self.story_id)
        submissions = factories.SubmissionFactory.create_batch(5, story=story)
        for submission in submissions:
            waypoints = factories.WaypointFactory.create_batch(5, submission=submission)
    def test_setup(self):
        self.assertEqual(models.Story.objects.all()[0].id, self.story_id)

class StoryTestCase(TestCase):
    def test_something(self):
        story = StoryFactory.create_batch(3)

class UserTestCase(TestCase):
    def test_creation(self):
        user = UserFactory.create_batch(5)
        users = User.objects.all()
        self.assertEqual(users.count(), 5)
        self.assertIsNotNone(users[0].id)
        self.client = Client()
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

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

class SubmissionTestCase(TestCase):
    def test_something(self):
        submission = SubmissionFactory.create()
        all_entries= models.Submission.objects.all()
        #maybe test many to one relationship
    def test_submission(self):
        story = StoryFactory.create()
        user = UserFactory.create()
        submission = SubmissionFactory.create(story = story, user = user)
        self.assertEqual(submission.story, story)
        self.assertEqual(submission.user, user)
        waypoint = WaypointFactory.create_batch(5, submission=submission)
        waypoints = Waypoint.objects.all()
        submissions = Submission.objects.all()
