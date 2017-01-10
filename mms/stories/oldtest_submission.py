from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import UserSerializer
import factory
import factory.fuzzy
from .models import Submission
from tests import SubmissionFactory
#from django.test import Client

class CreateSubmission(APITestCase):
    def test_can_create_submission(self):
        submission = SubmissionFactory.build()
        self.data = {'user': submission.user, 'story': submission.story}
        response = self.client.post('/submissions/', self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ReadSubmission(APITestCase):
    def test_can_read_submission (self):
        submission = SubmissionFactory.create()
        response = self.client.get('/submissions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# class UpdateSubmission(APITestCase):
#     def test_can_update_submission(self):
#         submission = SubmissionFactory.create()
#         self.data = {'user': submission.user, 'story': 'newstory'}
#         update = self.client.put('/submissions/{}/'.format(submission.id), self.data)
#         self.assertEqual(update.status_code, status.HTTP_200_OK)
#         response = self.client.get('/submissions/{}/'.format(submission.id))
#         self.assertTrue(response.data['instructions'] == 'newstory')

# class DeleteStory(APITestCase):
#     def test_can_delete_submission(self):
#         submission = SubmissionFactory.create_batch(5)
#         submissions = Submission.objects.all()
#         before = Submission.objects.count()
#         self.data = {'user': submissions[0].user, 'story': submissions[0].story}
#         delete = self.client.delete('submissions/{}/'.format(submissions[0].id), self.data)
#         after = Submission.objects.count()
#         self.assertEqual(delete.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertTrue(before > after)
