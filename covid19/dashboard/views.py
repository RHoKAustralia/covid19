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
        context['sore_none'] = Answer.objects.filter(question__question="Sore-throat").filter(scale_Answer=0)
        context['sore_mild'] = Answer.objects.filter(question__question="Sore-throat").filter(scale_Answer=1)
        context['sore_moderate'] = Answer.objects.filter(question__question="Sore-throat").filter(scale_Answer=2)
        context['sore_severe'] = Answer.objects.filter(question__question="Sore-throat").filter(scale_Answer=3)
        context['head_none'] = Answer.objects.filter(question__question="Headache").filter(scale_Answer=0)
        context['head_mild'] = Answer.objects.filter(question__question="Headache").filter(scale_Answer=1)
        context['head_moderate'] = Answer.objects.filter(question__question="Headache").filter(scale_Answer=2)
        context['head_severe'] = Answer.objects.filter(question__question="Headache").filter(scale_Answer=3)
        print("return custom context")
        return context


import django_tables2 as tables

class AnswerListView(generic.ListView):
    model = Answer
    template_name = 'dashboard_table.html'


class AnswerListView2(generic.ListView):
    template_name = 'dashboard_table.html'

    def get_queryset(self):
        from django.db.models import F
        first = F('participant__firstName')
        last = F('participant__lastName')
        # this won't work because of the bug in the models:
        #date = F('answerset__dateAnswered')
        query_set = Answer.objects.select_related('participant',
                'answerset').values(first=first, last=last)
        # , date=date)
