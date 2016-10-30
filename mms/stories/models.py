import datetime

from django.db import models
from django.utils import timezone

#deprecated
class Prompt(models.Model):
    prompt_text = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created')
    def __unicode__(self):
        return self.prompt_text
#deprecated
class Response(models.Model):
    prompt = models.ForeignKey(Prompt)
    response_text = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    submit_date = models.DateTimeField('date submitted', default=timezone.now())
    story_date = models.DateTimeField('story date', default=timezone.now())
    def __unicode__(self):
        return self.response_text

class Story(models.Model):
    story_name = models.CharField(max_length=200)
    story_description = models.TextField()
    story_instructions = models.TextField()

class User(models.Model):
    story_id = models.ForeignKey(Story)
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=254)

class Waypoint(models.Model):
    geom = models.CharField(max_length=200)
    notes = models.TextField()
    path_order = models.IntegerField(default=0)

class Submission(models.Model):
    story_users_count = models.IntegerField(default=0)
    user_id = models.ForeignKey(User)
    story_id = models.ForeignKey(Story)
    waypoint_id = models.ForeignKey(Waypoint)
