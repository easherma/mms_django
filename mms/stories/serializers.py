#from django.contrib.auth.models import User
from rest_framework import serializers
from stories.models import Story, StoryUser, Submission, Waypoint
#from rest_framework_gis.serializers import GeoFeatureModelSerializer

class StorySerializer(serializers.HyperlinkedModelSerializer):
    submissions = serializers.HyperlinkedRelatedField(many=True, view_name='submission-detail', queryset = Submission.objects.all(), allow_null=True)
    owner = serializers.HyperlinkedRelatedField(many=True, view_name='storyuser-detail', queryset = StoryUser.objects.all(), allow_null=True)
    class Meta:
        model = Story
        fields = ('url', 'name', 'description', 'instructions', 'submissions', 'owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    submissions = serializers.HyperlinkedRelatedField(many=True, view_name='submission-detail', queryset = Submission.objects.all(), allow_null=True)
    class Meta:
        model = StoryUser
        fields = ('url','username', 'email', 'submissions')

class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    waypoints = serializers.HyperlinkedRelatedField(many=True, view_name='waypoint-detail', queryset = Waypoint.objects.all(), allow_null=True)
    class Meta:
        model = Submission
        fields = ('url','user', 'story', 'waypoints')

class WaypointSerializer(serializers.HyperlinkedModelSerializer):
    # users = UserSerializer(many=True)
    # story = StorySerializer()
    class Meta:
        model = Waypoint
        #geo_field = "geom"
        fields = ('url', 'geom', 'notes', 'lng', 'lat', 'path_order', 'submission')

class WaypointsSerializer(serializers.HyperlinkedModelSerializer):
    # users = UserSerializer(many=True)
    # story = StorySerializer

    class Meta:
        model = Waypoint
        fields = ('url', 'geom', 'notes', 'lng', 'lat', 'path_order', 'submission__user')
