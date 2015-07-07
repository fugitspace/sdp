from django.conf import settings
from django.conf.urls import include, url
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),    
    url(r'^register/$', views.PersonCreateView.as_view(), name='create_person'),
    url(r'^update/(?P<pk>\d+)/$', views.PersonUpdateView.as_view(), name='update_person'),
    url(r'^(?P<pk>\d+)/profile/$', views.PersonDetailView.as_view(), name='person_profile'),
    
    url(r'^(?P<pk>\d+)/vitals/$', views.PersonVitalsCreate.as_view(), name='create_vitals'),
    url(r'^update/vitals/(?P<pk>\d+)/$', views.PersonVitalsUpdate.as_view(), name='update_vitals'),

    url(r'^profile/(?P<pk>\d+)/contacts/$', views.PersonContactsCreate.as_view(), name='create_contact'),
    url(r'^update/contacts/(?P<pk>\d+)/$', views.PersonContactsUpdate.as_view(), name='update_contact'),

    url(r'^profile/(?P<pk>\d+)/demographic/$', views.PersonDemographicCreate.as_view(), name='create_demographic'),
    url(r'^update/demographic/(?P<pk>\d+)/$', views.PersonDemographicUpdate.as_view(), name='update_demographic'),

    url(r'^profile/(?P<pk>\d+)/guardian/$', views.PersonGuardianCreate.as_view(), name='create_guardian'),
    url(r'^update/guardian/(?P<pk>\d+)/$', views.PersonGuardianUpdate.as_view(), name='update_guardian'),
]
