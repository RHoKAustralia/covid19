from django.shortcuts import render

# Create your views here.

from django.urls import path

from . import views
from . import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('questionnaire', views.IndexView.as_view(), name='anonymous'),
    path('monitor', views.TrackedView.as_view(), name='tracked'),
    path('saveresponse', views.QuestionnaireView.home, name='saveresponse'),
    path('<int:question_id>/', views.ScaleView.as_view(), name='form'),
]
