from django.test import TestCase
import factory
import factory.fuzzy
import geojson
import json
from . import models
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.test import Client
from django.contrib.auth.models import User
from tests import StoryFactory
from tests import StoryUserFactory
from tests import SubmissionFactory
from tests import WaypointFactory

class FunctionalTests(APITestCase):
    def setup(self):
        StoryFactory.create()
        StoryUserFactory.create_batch(5)
        SubmissionFactory.create()
        WaypointFactory.create_batch(10)
