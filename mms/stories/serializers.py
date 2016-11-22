from rest_framework import serializers
from stories.models import Waypoint


class WaypointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Waypoint
        fields = ('geom', 'notes', 'lng', 'lat', 'path_order', 'submission')

class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ('url', 'name')
