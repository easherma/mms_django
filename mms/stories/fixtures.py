from django.test import TestCase
import factory
import factory.fuzzy
import geojson
import json
from mms.stories import models
from .models import Story
from .models import Waypoint
from .models import Submission
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.test import Client
from django.contrib.auth.models import User

#@TODO want to be able to run this on the command line to generate test data
if __name__ == '__main__':
    generate_fixtures(self)

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.fuzzy.FuzzyText(length=12, prefix='')
    email = factory.LazyAttribute(lambda a: u'{0}@example.com'.format(a.username).lower())
    id = factory.fuzzy.FuzzyInteger(0, 256)
    story = factory.RelatedFactory(StoryFactory)
    User.objects.create_user(self.username, self.email, factory.fuzzy.FuzzyText(length=12, prefix=''))

    user = factory.SubFactory(StoryUserFactory)

class StoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Story
    name= factory.fuzzy.FuzzyText(length=8, prefix='')
    description= factory.fuzzy.FuzzyText(length=250, prefix='')
    instructions= factory.fuzzy.FuzzyText(length=350, prefix='')
    owner= factory.SubFactory(UserFactory)
    #these were nifty but seemed less useful
    @factory.post_generation
    def create_submissions(self, create, extracted, **kwargs):
        #self.owner = UserFac#tory.create()
        if not create:
            return
        #id = factory.fuzzy.FuzzyInteger(0, 256)
        #submission_id = id.fuzz()
        submissions = SubmissionFactory.create_batch(2, story=self)
        #for submission in submissions:
        #    print(submission)
        #    waypoints = WaypointFactory.create_batch(4, submission=self.submission)
        # for i in range(10):
        #     submission = SubmissionFactory.create(story=self)
        #     waypoints = WaypointFactory.create_batch(4)

class SubmissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Submission
    user = factory.SubFactory(UserFactory)
    story = factory.SubFactory(StoryFactory)
    #these were nifty but seemed less useful
    id = factory.fuzzy.FuzzyInteger(0, 256)
    @factory.post_generation
    def create_waypoints(self, create, extracted, **kwargs):
        #self.owner = UserFac#tory.create()
        if not create:
            return
        waypoints = WaypointFactory.create_batch(4, submission=self)

class WaypointFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Waypoint
    id = factory.fuzzy.FuzzyInteger(0, 256)
    waypoint = geojson.utils.generate_random("Point")
    geom = geojson.utils.generate_random("Point")
    lng = waypoint.coordinates[0]
    lat = waypoint.coordinates[1]
    notes = factory.fuzzy.FuzzyText(length=8, prefix='')
    path_order = factory.fuzzy.FuzzyInteger(0, 6)
    #these were nifty but seemed less useful
    submission = factory.SubFactory(SubmissionFactory)
    submission = factory.SubFactory(SubmissionFactory, submission=factory.SelfAttribute('..submission'))
    @factory.post_generation
    def create_waypoints(self, create, extracted, **kwargs):
        if not create:
            return
        waypoints = WaypointFactory.create_batch(4, )

def generate_fixtures(self):
    id = factory.fuzzy.FuzzyInteger(0, 256)
    self.story_id = id.fuzz()
    story = factories.StoryFactory.create_batch(5, id=id.fuzz())
