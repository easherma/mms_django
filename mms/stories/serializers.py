#from django.contrib.auth.models import User
from rest_framework import serializers
from stories.models import Story, User, Waypoint

class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ('url', 'name', 'description', 'instructions')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','story', 'name', 'email')

class WaypointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Waypoint
        fields = ('url', 'geom', 'notes', 'lng', 'lat', 'path_order', 'submission')
