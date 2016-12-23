from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import UserSerializer
import factory
import factory.fuzzy
from . import models
from .models import StoryUser
from .models import Waypoint
from .models import Submission
from tests import StoryUserFactory
#from django.test import Client

class CreateUserTest(APITestCase):
    def test_can_create_user(self):
        user = StoryUserFactory.create()
        #random example works if its hardcoded
        self.data = {'username': user.username, 'email': 'anvonwxcgttq@example.com'}
        print self.data
        #@TODO should be this:
        #self.data = {'username': str(user.username), 'email': user.email}
        response = self.client.post('/users/', self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print "create user ok"
