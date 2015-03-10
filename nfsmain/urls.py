from django.conf.urls import patterns, url

from nfsmain import views

urlpatterns = \
    patterns('',
             url(r'^$', views.index, name='index'),
             url(r'^facts/$', views.FactListView.as_view(), name='fact_list'),
             url(r'^facts/add/$', views.FactCreateView.as_view(), name='fact_add'),
             url(r'^facts/(?P<pk>\d+)$', views.FactDetailView.as_view(), name='fact_view')
             )
