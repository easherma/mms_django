from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    url(r'^', include('stories.urls')),
]