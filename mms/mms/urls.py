from django.conf.urls import url, include
from rest_framework import routers
from stories import views
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from mms.views import HomePageView, StoryPageView


schema_view = get_schema_view(title='Map My Story API View')

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
#router.register(r'userdetail', views.UserDetail.as_view({'get': 'list'}), base_name='')
router.register(r'stories', views.StoryViewSet)
router.register(r'submissions', views.SubmissionViewSet)
router.register(r'waypoints', views.WaypointViewSet)
#router.register(r'^stories/(?P<name>.+)/$', views.StoryViewSet)



api_patterns = [
    url(r'^', include(router.urls)),
    #url('^testview/$', views.WaypointsByStory),
    #url('^stories/(?P<pk>.+)/$', views.StoryViewSet.as_view({'get': 'list'})),
    url('^schema/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = [
    #url(r'^(?P<name>pattern)/$', views.StoryViewSet.as_view({'get': 'list'})),
    url(r'^$', HomePageView.as_view()),
    url(r'^stories/(?P<pk>\d+)/$', StoryPageView.as_view()),
    #url(r'^stories/(?P<pk>.+)/$', StoryPageView.as_view(), name = 'story'),
    url(r'^api/', include(api_patterns))

]
