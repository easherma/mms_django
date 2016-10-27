from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.StoriesListView.as_view(), name='stories-list'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<response_id>[0-9]+)/count/$', views.count, name='count'),
]