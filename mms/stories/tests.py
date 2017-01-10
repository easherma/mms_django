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
