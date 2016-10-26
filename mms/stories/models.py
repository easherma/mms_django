import datetime

from django.db import models
from django.utils import timezone

class Prompt(models.Model):
    prompt_text = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created')
    def __unicode__(self):
        return self.prompt_text
    
class Response(models.Model):
    prompt = models.ForeignKey(Prompt)
    response_text = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    submit_date = models.DateTimeField('date submitted', default=timezone.now())
    story_date = models.DateTimeField('story date', default=timezone.now())
    def __unicode__(self):
        return self.response_text

class User(models.Model):
    # can some of these be stored as JSON/is that useful?
    story_id = models.ForeignKey(Response)
    row_id = #uniqueid/inncrement
    user_id = #uniqueid/inncrement
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=254)
    path_order = models.IntegerField(default=0)
    geom(point) = #discuss
    notes = models.CharField(max_length=200)
    submit_date = models.DateTimeField('date submitted', default=timezone.now())
    story_date = models.DateTimeField('story date', default=timezone.now())
    def __unicode__(self): 
        return self.user_id
    
