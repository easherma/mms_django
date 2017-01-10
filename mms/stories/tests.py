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
    def setUp(self):
        id = factory.fuzzy.FuzzyInteger(0, 256)
        self.story_id = id.fuzz()
        story = factories.StoryFactory.create(id=self.story_id)
        submissions = factories.SubmissionFactory.create_batch(5, story=story)
        for submission in submissions:
            waypoints = factories.WaypointFactory.create_batch(5, submission=submission)

    def test_setup(self):
        self.assertEqual(models.Story.objects.all()[0].id, self.story_id)
    def test_matching_ids(self):
        #Submission.objects.filter(story=story).values_list('pk', flat=True)
        self.assertEqual(models.Story.objects.all()[0].id, self.story_id)



        #maybe test many to one relationship
    # def test_submission(self):
    #     story = StoryFactory.create()
    #     user = StoryUserFactory.create()
    #     submission = SubmissionFactory.create(story = story, user = user)
    #     self.assertEqual(submission.story, story)
    #     self.assertEqual(submission.user, user)
    #     waypoint = WaypointFactory.create_batch(5, submission=submission)
    #     waypoints = Waypoint.objects.all()
    #     submissions = Submission.objects.all()


#class OutputTestCase(TestCase):

    #def geojson(self):
        #create story
        #users in story
        #waypoints for each user (submissions?)
        #query object, parse into geojson
        #make a route that prints the geojson
