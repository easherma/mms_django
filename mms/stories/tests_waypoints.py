from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import UserSerializer
import factory
import factory.fuzzy
from .models import Waypoint
from tests import WaypointFactory
from .models import StoryUser
from tests import StoryUserFactory
#from django.test import Client

class CreateWaypoint(APITestCase):
    def test_can_create_Waypoint(self):
        stoy = StoryUserFactory.create()
        waypoint = WaypointFactory.build()
        self.data = {'geom': waypoint.geom, 'notes': waypoint.notes, 'lng': waypoint.lng, 'lat': waypoint.lat, 'path_order': waypoint.path_order, 'submission': waypoint.submission}
        response = self.client.post('/waypoints/', self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ReadWaypoint(APITestCase):
    def test_can_read_waypoint(self):
        waypoint = WaypointFactory.create()
        response = self.client.get('/waypoints/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #print response

#put not allowed atm
# class UpdateWaypoint(APITestCase):
#     def test_can_update_waypoint(self):
#         waypoint = WaypointFactory.create_batch(5)
#         waypoints = Waypoint.objects.all()
#         #select first created user
#         change = Waypoint.objects.filter(submission=waypoints[0].submission).update(notes='changed')
#         self.data = {'geom': waypoints[0].geom, 'notes': waypoints[0].notes, 'lng': waypoints[0].lng, 'lat': waypoints[0].lat, 'path_order': waypoints[0].path_order, 'submission': waypoints[0].submission}
#         update = self.client.put('/waypoints/{}/'.format(waypoints[0].id), self.data)
#         self.assertEqual(update.status_code, status.HTTP_200_OK)

#delete not allowed atm
# class DeleteWaypoint(APITestCase):
#     def test_can_delete_waypoint(self):
#         waypoint = WaypointFactory.create_batch(5)
#         waypoints = Waypoint.objects.all()
#         before = Waypoint.objects.count()
#         self.data = {'geom': waypoints[0].geom, 'notes': waypoints[0].notes, 'lng': waypoints[0].lng, 'lat': waypoints[0].lat, 'path_order': waypoints[0].path_order, 'submission': waypoints[0].submission}
#         delete = self.client.delete('/waypoints/{}/'.format(waypoints[0].id), self.data)
#         after = Waypoint.objects.count()
#         self.assertEqual(delete.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertTrue(before > after)
