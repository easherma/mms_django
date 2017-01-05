import datetime
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class StoryUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    USERNAME_FIELD = 'email'
    # @TODO def get_waypoints():



class Story(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField()
    user = models.ForeignKey(StoryUser, null = True)
    def __unicode__(self):
        return self.name
    @classmethod
    def waypoints():
        story = Story.objects.all()

class Submission(models.Model):
    user = models.ForeignKey(StoryUser)
    story = models.ForeignKey(Story)

class Waypoint(models.Model):
    geom = models.CharField(max_length=200)
    notes = models.TextField()
    lng = models.DecimalField(max_digits=8, decimal_places=5)
    lat = models.DecimalField(max_digits=8, decimal_places=5)
    path_order = models.IntegerField(default=0)
    submission = models.ForeignKey(Submission, null=True)
    # def __unicode__(self):
    #     return "Waypoint: {}, {}".format(self.lng, self.lat)
