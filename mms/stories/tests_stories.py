from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import UserSerializer
import factory
import factory.fuzzy
from .models import Story
from stories.factories import StoryFactory
#from django.test import Client

class CreateStory(APITestCase):
    def test_can_create_story(self):
        story = StoryFactory.build()
        self.data = {'name': story.name, 'description': story.description, 'instructions': story.instructions}
        response = self.client.post('/stories/', self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ReadStory(APITestCase):
    def test_can_read_story(self):
        story = StoryFactory.create()
        response = self.client.get('/stories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UpdateStory(APITestCase):
    def test_can_update_story(self):
        story = StoryFactory.create()
        self.data = {'name': story.name, 'description': story.description, 'instructions': 'dothis'}
        update = self.client.put('/stories/{}/'.format(story.id), self.data)
        self.assertEqual(update.status_code, status.HTTP_200_OK)
        response = self.client.get('/stories/{}/'.format(story.id))
        self.assertTrue(response.data['instructions'] == 'dothis')

class DeleteStory(APITestCase):
    def test_can_delete_story(self):
        story = StoryFactory.create_batch(5)
        stories = Story.objects.all()
        before = Story.objects.count()
        self.data = {'name': stories[0].name, 'description': stories[0].description, 'instructions': stories[0].instructions}
        delete = self.client.delete('/stories/{}/'.format(stories[0].id), self.data)
        after = Story.objects.count()
        self.assertEqual(delete.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(before > after)
