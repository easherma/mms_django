

from django.db import models
from django.utils import timezone


class Story(models.Model):
    story_name = models.CharField(max_length=200)
    story_description = models.TextField()
    story_instructions = models.TextField()
    def __unicode__(self):
        return self.story_name

class User(models.Model):
    story_id = models.ForeignKey(Story)
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=254)
    def __unicode__(self):
        return self.user_name
class Waypoint(models.Model):
    geom = models.CharField(max_length=200)
    notes = models.TextField()
    lng = models.DecimalField(max_digits=8, decimal_places=5)
    lat = models.DecimalField(max_digits=8, decimal_places=5)
    path_order = models.IntegerField(default=0)
    def __unicode__(self):
        return self.geom
class Submission(models.Model):
    story_users_count = models.IntegerField(default=0)
    user_id = models.ForeignKey(User)
    story_id = models.ForeignKey(Story)
    waypoint_id = models.ForeignKey(Waypoint)
    def __unicode__(self):
        return self.user_id
