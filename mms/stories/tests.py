from django.test import TestCase
import factory
import factory.fuzzy
import geojson
from . import models

class StoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Story
    story_name= factory.fuzzy.FuzzyText(length=8, prefix='')
    story_description= factory.fuzzy.FuzzyText(length=250, prefix='')
    story_instructions= factory.fuzzy.FuzzyText(length=350, prefix='')

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User
    story_id = factory.SubFactory(StoryFactory)
    user_name = factory.fuzzy.FuzzyText(length=12, prefix='')
    user_email = factory.LazyAttribute(lambda a: '{0}@example.com'.format(a.user_name).lower())

class WaypointFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Waypoint
    geom = geojson.utils.generate_random("Point")
    lng = factory.fuzzy.FuzzyDecimal(-180, 180, precision=5)
    lat = factory.fuzzy.FuzzyDecimal(-90, 90, precision=5)    
    notes = factory.fuzzy.FuzzyText(length=8, prefix='')
    path_order = factory.fuzzy.FuzzyInteger(0, 6)

class SubmissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Submission
    story_users_count = factory.fuzzy.FuzzyInteger(0, 30)
    user_id = factory.SubFactory(UserFactory)
    story_id = factory.SubFactory(StoryFactory)
    waypoint_id = factory.SubFactory(WaypointFactory)


class StoryTestCase(TestCase):
    def test_something(self):
        story = StoryFactory.create()

class UserTestCase(TestCase):
    def test_something(self):
        user = UserFactory.create()

class WaypointTestCase(TestCase):
    def test_something(self):
        waypoint = WaypointFactory.create()
        print models.Waypoint.objects.all()

class SubmissionTestCase(TestCase):
    def test_something(self):
        submission = SubmissionFactory.create()
    def test_output(self):
        #import pdb; pdb.set_trace()
        submission = SubmissionFactory.create()
        print models.Submission.objects
