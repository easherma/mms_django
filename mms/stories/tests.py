from django.test import TestCase
import factory
import factory.fuzzy
import geojson
from . import models
from .models import User
from .models import Waypoint

class StoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Story
    name= factory.fuzzy.FuzzyText(length=8, prefix='')
    description= factory.fuzzy.FuzzyText(length=250, prefix='')
    instructions= factory.fuzzy.FuzzyText(length=350, prefix='')

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User
    story = factory.SubFactory(StoryFactory)
    name = factory.fuzzy.FuzzyText(length=12, prefix='')
    email = factory.LazyAttribute(lambda a: '{0}@example.com'.format(a.name).lower())


class SubmissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Submission
    user = factory.SubFactory(UserFactory)
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
        user = UserFactory.create_batch(5)
        users = User.objects.all()
        self.assertEqual(users.count(), 5)
        self.assertIsNotNone(users[0].id)

class WaypointTestCase(TestCase):
    def test_something(self):
        #waypoint = WaypointFactory.create_batch(5)
        waypoint = WaypointFactory.create()
        waypoints = Waypoint.objects.all()
    def test_multWaypointForSubmission(self):
        #waypoint = WaypointFactory.create_batch(5)
        submission = SubmissionFactory.create()
        waypoint = WaypointFactory.create_batch(5, submission=submission)
        waypoints = Waypoint.objects.all()
        self.assertIsNotNone(waypoints[0].id)
        self.assertEqual(waypoints[0].submission, submission)
        self.assertEqual(waypoints.count(), 5)
        for waypoint in waypoints:
            self.assertEqual(waypoint.submission, submission)
            print waypoint.id, submission.id

class SubmissionTestCase(TestCase):
    def test_something(self):
        submission = SubmissionFactory.create_batch(5)
        all_entries= models.Submission.objects.all()



class OutputTestCase(TestCase):

    def test_get_profile_stats(self):
        profiles = []
        profiles.extend(SubmissionFactory.create_batch(4))
        #print profiles
