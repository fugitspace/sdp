from django.conf import settings
from django.conf.urls import include, url
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    url(r'^', views.IndexView.as_view(), name='index'),    
    url(r'^register/$', views.PersonCreateView.as_view(), name='create_person'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.PersonUpdateView.as_view(), name='update_person'),
]
