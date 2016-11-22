from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from stories import views

urlpatterns = [
  url(r'^stories/$', views.WaypointList.as_view()),
  url(r'^snippets/(?P<pk>[0-9]+)/$', views.WaypointDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns = [
#     url(r'^$', views.StoriesListView.as_view(), name='stories-list'),
#     url(r'^$', views.IndexView.as_view(), name='index'),
#     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#     #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#     #url(r'^(?P<response_id>[0-9]+)/count/$', views.count, name='count'),
# ]
