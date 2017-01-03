from django.conf.urls import url, include
from rest_framework import routers
from stories import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Map My Story API View')

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'stories', views.StoryViewSet)
router.register(r'submissions', views.SubmissionViewSet)
router.register(r'waypoints', views.WaypointViewSet)




urlpatterns = [
    url(r'^', include(router.urls)),
    #url('^testview/$', views.WaypointsByStory),
    url('^testview/$', views.WaypointsByStory.as_view()),
    url('^schema/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
