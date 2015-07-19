
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^news/$', views.news, name='news'),
	url(r'^([0-9]+)/$', views.post_detail, name='detail'),
	
]
