from django.conf.urls import url, include
from rest_framework import routers
from stories import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
#router.register(r'userdetail', views.UserDetail.as_view({'get': 'list'}), base_name='')
router.register(r'stories', views.StoryViewSet)
router.register(r'submissions', views.SubmissionViewSet)
router.register(r'waypoints', views.WaypointViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^userdetail$', views.UserDetail.as_view({'get': 'list'}))
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
