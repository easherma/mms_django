from django.test import TestCase
import factory
from . import models

class StoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = model.Story
    story_name= factory.fuzzy.FuzzyText(length=8, chars=string.ascii_letters, prefix='')
    story_description= factory.fuzzy.FuzzyText(length=250, chars=string.ascii_letters, prefix='')
    story_instructions= factory.fuzzy.FuzzyText(length=350, chars=string.ascii_letters, prefix='')

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = model.User
    story_id = factory.SubFactory(StoryFactory)
    user_name = factory.fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    user_email = email = factory.LazyAttribute(lambda a: '{0}.{1}@example.com'.format(a.first_name).lower())

class WaypointFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = model.Waypoint
    geom = factory.fuzzy.FuzzyText(length=100, chars=string.ascii_letters, prefix='')
    notes = factory.fuzzy.FuzzyText(length=8, chars=string.ascii_letters, prefix='')
    path_order = FuzzyInteger(0, 6)

class SubmissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = model.Submission
    story_users_count = models.IntegerField(default=0)
    owner = factory.SubFactory(OwnerFactory)
    user_id = factory.SubFactory(UserFactory)
    story_id = factory.SubFactory(StoryFactory)
    waypoint_id = factory.SubFactory(WaypointFactory)
