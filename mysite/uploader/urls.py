
from django.conf.urls import url

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.uploads, name='uploads'),
    url(r'^(.+)/$', views.documents_by_category, name='documents_by_category')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
