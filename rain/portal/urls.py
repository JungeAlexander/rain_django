from django.conf.urls import url

from . import views

app_name = 'portal'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /portal/interaction/5/
    url(r'^interaction/(?P<interaction_id>[0-9]+)/$', views.interaction_detail, name='interaction_detail'),
    # ex: /portal/rna/3/
    url(r'^rna/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='rna_detail'),
    # ex: /portal/rna/3/description/
    url(r'^rna/(?P<rna_id>[0-9]+)/description/$', views.rna_description, name='rna_description'),
    # ex: /portal/rna/3/vote/
    url(r'^rna/(?P<rna_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /portal/rna/3/results/
    url(r'^rna/(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
]
