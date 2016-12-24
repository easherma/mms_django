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

class CreateUser(APITestCase):
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

class ReadUser(APITestCase):
    def test_can_read_user(self):
        user = StoryUserFactory.create()
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #print response

class UpdateUser(APITestCase):
    def test_can_update_user(self):
        user = StoryUserFactory.create_batch(5)
        users = StoryUser.objects.all()
        #select first created user
        change = StoryUser.objects.filter(username=users[0].username).update(username='changed')
        changed =
        for user in users:
            print user.username
        #selected =  StoryUser.objects.get('username'=users.username )
        #@TODO, not sure I'mm approaching this correctly, may need to update the view?
        response = self.client.put('/users/', )
        #obj.objects.update({'username': 'changed'})
