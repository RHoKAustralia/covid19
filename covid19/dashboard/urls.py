from django.shortcuts import render

# Create your views here.

from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('graph', TemplateView.as_view(template_name='dashboard/dashboard.html')),
    path('map', TemplateView.as_view(template_name='dashboard/dashboard.html')),
    path('table', views.AnswerListView.as_view(), name='table'),
    path('', views.IndexView.as_view(), name='index'),
]
