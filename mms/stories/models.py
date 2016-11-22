import datetime

from django.db import models
from django.utils import timezone


class Story(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField()
    def __unicode__(self):
        return self.name

class User(models.Model):
    story = models.ForeignKey(Story)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    def __unicode__(self):
        return self.name
        
class Submission(models.Model):
    user = models.ForeignKey(User)
    story = models.ForeignKey(Story)

class Waypoint(models.Model):
    geom = models.CharField(max_length=200)
    notes = models.TextField()
    lng = models.DecimalField(max_digits=8, decimal_places=5)
    lat = models.DecimalField(max_digits=8, decimal_places=5)
    path_order = models.IntegerField(default=0)
    submission = models.ForeignKey(Submission, null=True)
    def __unicode__(self):
        return "Waypoint: {}".format(self.id)
