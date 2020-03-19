from django.shortcuts import render

# Create your views here.

from django.urls import path, re_path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard/dashboard_gallery.html')),
    path('graph', views.IndexView.as_view(), name='index'),
    re_path('participant/$', views.ParticipantView.as_view(), name='participant'),
    re_path(r'participant/(?P<pk>[A-Za-z\-0-9]+)/$', views.ParticipantView.as_view(), name='participantfor'),

    # inactive
    path('map', TemplateView.as_view(template_name='dashboard/dashboard.html')),
    path('table', views.AnswerListView.as_view(), name='table'),
    path('table2', views.AnswerListView2.as_view(), name='table2'),

    #path('graph', TemplateView.as_view(template_name='dashboard/dashboard.html')),
]
