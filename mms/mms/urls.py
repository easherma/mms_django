from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^stories/', include('stories.urls', namespace="stories")),
    url(r'^admin/', include(admin.site.urls)),
    
]