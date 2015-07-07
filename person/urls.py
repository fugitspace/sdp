from django.conf import settings
from django.conf.urls import include, url
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),    
    url(r'^register/$', views.PersonCreateView.as_view(), name='create_person'),
    url(r'^profile/(?P<pk>\d+)/$', views.PersonDetailView.as_view(), name='person_profile'),
    url(r'^profile/(?P<pk>\d+)$', views.PersonDetailView.as_view(), name='profile_section'),
    url(r'^update/(?P<pk>\d+)/$', views.PersonUpdateView.as_view(), name='update_person'),
]
