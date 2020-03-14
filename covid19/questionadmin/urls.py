from django.shortcuts import render

# Create your views here.

from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:question_id>/', views.ScaleView.as_view(), name='form'),
]
