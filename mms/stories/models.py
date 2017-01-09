import datetime
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Story(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField()

    def __unicode__(self):
        return self.name
    # @classmethod
    # def waypoints():
    #     story = Story.objects.all()
class StoryUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    USERNAME_FIELD = 'email'
    story = models.ForeignKey(Story, null = True, related_name='owner')
    # @TODO def get_waypoints():



class Submission(models.Model):
    user = models.ForeignKey(StoryUser, related_name='submissions', on_delete=models.CASCADE)
    story = models.ForeignKey(Story , related_name='submissions', on_delete=models.CASCADE)

class Waypoint(models.Model):
    waypoint = models.CharField(max_length=200 , blank=False)
    geom = models.CharField(max_length=200 , blank=False)
    notes = models.TextField()
    lng = models.DecimalField(max_digits=8, decimal_places=5, blank=False)
    lat = models.DecimalField(max_digits=8, decimal_places=5, blank=False)
    path_order = models.IntegerField(default=0)
    submission = models.ForeignKey(Submission, null=True, related_name='waypoints', on_delete=models.CASCADE, blank=False)
    # def __unicode__(self):
    #     return "Waypoint: {}, {}".format(self.lng, self.lat)
