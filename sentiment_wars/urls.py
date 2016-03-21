from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'sentiment_wars.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'^analysis/', include('analysis.urls')),	
#	url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
