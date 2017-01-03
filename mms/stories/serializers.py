#from django.contrib.auth.models import User
from rest_framework import serializers
from stories.models import Story, StoryUser, Submission, Waypoint
#from rest_framework_gis.serializers import GeoFeatureModelSerializer

class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ('url', 'name', 'description', 'instructions')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StoryUser
        fields = ('url','username', 'email')

class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Submission
        fields = ('url','user', 'story')

class WaypointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Waypoint
        #geo_field = "geom"
        fields = ('url', 'geom', 'notes', 'lng', 'lat', 'path_order', 'submission')

class WaypointsSerializer(serializers.ModelSerializer):
    waypoints = serializers.StringRelatedField(many=True)

    class Meta:
        model = Story
        fields = ('url', 'name', 'description', 'instructions')
        
