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
        user = StoryUserFactory.build()
        self.data = {'username': user.username, 'email': user.email}
        response = self.client.post('/users/', self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

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
        self.data = {'username': users[0].username, 'email': users[0].email}
        update = self.client.put('/users/{}/'.format(users[0].id), self.data)
        self.assertEqual(update.status_code, status.HTTP_200_OK)

class DeleteUser(APITestCase):
    def test_can_update_user(self):
        user = StoryUserFactory.create_batch(5)
        users = StoryUser.objects.all()
        before = StoryUser.objects.count()
        self.data = {'username': users[0].username, 'email': users[0].email}
        delete = self.client.delete('/users/{}/'.format(users[0].id), self.data)
        after = StoryUser.objects.count()
        self.assertEqual(delete.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(before > after)
