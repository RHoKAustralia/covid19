from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView

from questionadmin.models import Answer
from questionadmin.models import Question,QuestionType

# Create your views here.
class IndexView(generic.ListView):
    context_object_name = 'answers'
    def get_queryset(self):
        print("do the queryset\n")
        return Answer.objects.filter(question__question="Cough")

    def get_context_data(self,**kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['none'] = Answer.objects.filter(question__question="Cough").filter(scale_Answer=0)
        context['mild'] = Answer.objects.filter(question__question="Cough").filter(scale_Answer=1)
        context['moderate'] = Answer.objects.filter(question__question="Cough").filter(scale_Answer=2)
        context['severe'] = Answer.objects.filter(question__question="Cough").filter(scale_Answer=3)
        print("return custom context")
        return context


import django_tables2 as tables

class AnswerListView(generic.ListView):
    model = Answer
    template_name = 'dashboard_table.html'

