import datetime
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.forms import modelformset_factory

class Story(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField()
    owner = models.ForeignKey(User, related_name='owner', null = True,  blank=True)
    # @classmethod
    # def waypoints():
    #     story = Story.objects.all()

# class StoryUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     #email = models.ForeignKey(User)
#     USERNAME_FIELD = 'email'
#     story = models.ForeignKey(Story, null = True, related_name='owner')
#     # @TODO def get_waypoints():



class Submission(models.Model):
    user = models.ForeignKey(User, related_name='submissions', on_delete=models.CASCADE)
    story = models.ForeignKey(Story , related_name='submissions', on_delete=models.CASCADE)

class Waypoint(models.Model):
    waypoint = models.CharField(max_length=200 , blank=False)
    geom = models.CharField(max_length=200 , blank=False)
    notes = models.TextField()
    lng = models.DecimalField(max_digits=8, decimal_places=5, blank=False)
    lat = models.DecimalField(max_digits=8, decimal_places=5, blank=False)
    path_order = models.IntegerField(default=0)
    gid = models.TextField()
    label = models.TextField()
    submission = models.ForeignKey(Submission, null=True, related_name='waypoints', on_delete=models.CASCADE, blank=False)
    # def __unicode__(self):
    #     return "Waypoint: {}, {}".format(self.lng, self.lat)
