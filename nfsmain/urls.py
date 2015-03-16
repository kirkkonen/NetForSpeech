from django.conf.urls import patterns, url

from nfsmain import views

urlpatterns = \
    patterns('',
             url(r'^$', views.index, name='index'),
             url(r'^nfsadmin/$', views.index, name='admin'),
             url(r'^facts/$', views.FactListView.as_view(), name='fact_list'),
             url(r'^facts/add/$', views.FactCreateView.as_view(), name='fact_add'),
             url(r'^facts/(?P<pk>\d+)$', views.FactDetailView.as_view(), name='fact_detail'),
             url(r'^speakers/$', views.SpeakerListView.as_view(), name='speaker_list'),
             url(r'^speakers/add/$', views.SpeakerCreateView.as_view(), name='speaker_add'),
             url(r'^speakers/(?P<pk>\d+)$', views.SpeakerDetailView.as_view(), name='speaker_detail'),
             url(r'^statements/$', views.StatementListView.as_view(), name='statement_list'),
             url(r'^statements/add/$', views.StatementCreateView.as_view(), name='statement_add'),
             url(r'^statements/(?P<pk>\d+)$', views.StatementDetailView.as_view(), name='statement_detail'),
             url(r'^organisations/$', views.OrganisationListView.as_view(), name='organisation_list'),
             url(r'^organisations/add/$', views.OrganisationCreateView.as_view(), name='organisation_add'),
             url(r'^organisations/(?P<pk>\d+)$', views.OrganisationDetailView.as_view(), name='organisation_detail'),
             )
