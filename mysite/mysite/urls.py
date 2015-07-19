"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

# imports for the TemplateView shortcut
from django.views.generic import TemplateView

# imports for the MEDIA control
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	url(r'^$', include('blog.urls')),
	url(r'^blog/', include('blog.urls')),
	url(r'^guestbook/', include('guestbook.urls')),
    url(r'^documents/', include('uploader.urls')),
    url(r'^board/', include('board.urls')),
    url(r'^affald/$', TemplateView.as_view(template_name='affald.html'), name='affald'),
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^documents/', TemplateView.as_view(template_name='stat.html'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
