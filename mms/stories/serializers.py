#from django.contrib.auth.models import User
from rest_framework import serializers
from stories.models import Story, StoryUser, Submission, Waypoint

class StorySerializer(serializers.HyperlinkedModelSerializer):
    submissions = serializers.HyperlinkedRelatedField(many=True, view_name='submission-detail', queryset = Submission.objects.all(), allow_null=True)
    class Meta:
        model = Story
        fields = ('url', 'name', 'description', 'instructions', 'user', 'submissions')

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
        fields = ('url', 'geom', 'notes', 'lng', 'lat', 'path_order', 'submission')
