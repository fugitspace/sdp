from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static 
from django.views.generic import TemplateView

from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views


urlpatterns = [    
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^patient/', include('person.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
