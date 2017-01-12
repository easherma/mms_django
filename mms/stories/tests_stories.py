from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import UserSerializer
import factory
import factory.fuzzy
from .models import Story
from stories.factories import StoryFactory
from stories.factories import UserFactory
from django.test import Client

#TODO factory.build() breaks with Django 1.8?
#TODO reverse function dosent seem to work. not sure if i should use vanilla django or rest, and if the viewset affects it?
#TODO not sure i understand best practices of setting up these seperate tests vs other test, looks like data dosen't carry over
class StoryTests(APITestCase):
    # def setUp(self):
    #     owner = UserFactory.create()
    #     story = StoryFactory.create()
    def test_read_story(self):
        print(Story.objects.all().values())
        #story = StoryFactory.create()
        #url = reverse('/api/stories/')
        response = self.client.get('/api/stories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_can_create_story(self):
        #story= #print (Story.objects.all().values())
        story = StoryFactory.stub()
        owner = UserFactory.create()
        #self.data = {'name': 'My First Story', 'description': 'yourstory', 'instructions': 'put your dots on your maps and connect them with them lines', 'owner': owner}
        self.data = {'name': 'name', 'description': 'description', 'instructions': 'put your dots on your maps and connect them with them lines'}

        response = self.client.post('/api/stories/', self.data)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Story.objects.count(), 1)
        self.assertEqual(Story.objects.get().name, story.name)
"""
class ReadStory(APITestCase):
    def test_can_read_story(self):
        story = StoryFactory.create()
        response = self.client.get('/api/stories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UpdateStory(APITestCase):
    def test_can_update_story(self):
        story = StoryFactory.create()
        self.data = {'name': story.name, 'description': story.description, 'instructions': 'dothis', 'owner': story.owner}
        update = self.client.put('/api/stories/{}/'.format(story.id), self.data)
        self.assertEqual(update.status_code, status.HTTP_200_OK)
        response = self.client.get('/api/stories/{}/'.format(story.id))
        self.assertTrue(response.data['instructions'] == 'dothis')

class DeleteStory(APITestCase):
    def test_can_delete_story(self):
        story = StoryFactory.create_batch(5)
        stories = Story.objects.all()
        before = Story.objects.count()
        self.data = {'name': stories[0].name, 'description': stories[0].description, 'instructions': stories[0].instructions}
        delete = self.client.delete('/api/stories/{}/'.format(stories[0].id), self.data)
        after = Story.objects.count()
        self.assertEqual(delete.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(before > after)
"""
