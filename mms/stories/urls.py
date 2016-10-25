from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /stories/5/
    url(r'^(?P<prompt_id>[0-9]+)/$', views.prompts, name='prompts'),
    # ex: /stories/5/
    url(r'^(?P<prompt_id>[0-9]+)/$', views.prompt_detail, name='prompt_detail'),
    # ex: /stories/5/results/
    url(r'^(?P<prompt_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /stories/5/count/
    url(r'^(?P<prompt_id>[0-9]+)/count/$', views.count, name='count'),    
]