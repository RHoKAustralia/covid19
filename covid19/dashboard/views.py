from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView

from questionadmin.models import Answer
from questionadmin.models import Question,QuestionType
from questionadmin.models import Participant,ParticipantLocation,Location,Region,Country,AgeRanges,Country,AnswerSet

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

class AnswerTable(tables.Table):
    class Meta:
        model = Answer
        template_name = "dashboard_table.html"
        fields = ("question", "scale_Answer", )

from django_tables2 import SingleTableView
class AnswerListView(SingleTableView):
    model = Answer
    table_class = AnswerTable
    template_name = 'dashboard_table.html'


class AnswerListView2(generic.ListView):
    template_name = 'dashboard_table2.html'

    def get_queryset(self):
        from django.db.models import F
        first = F('participant__firstName')
        last = F('participant__lastName')
        # this won't work because of the bug in the models:
        #date = F('answerset__dateAnswered')
        query_set = Answer.objects.select_related('participant',
                'answerset').values(first=first, last=last)
        print("table2="+str(query_set))
        # , date=date)
        return query_set

def infofor(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
from django.template.defaulttags import register
@register.filter
def get_item(dictionary, key):
    return dictionary
class ParticipantView(generic.ListView):
    template_name = "dashboard_participant.html"
    context_object_name = 'participants'
    # additional parameters
    pk = None
    def get_queryset(self):
        if "pk" in self.kwargs:
            return Participant.objects.filter(trackingKey=self.kwargs["pk"])
        else:
            return Participant.objects.all()

    def get_context_data(self,**kwargs):
        context = super(ParticipantView,self).get_context_data(**kwargs)
        single = False
        if "pk" in self.kwargs:
            print("SINGLE PARTICIPANT")
            single = True
            participant = self.get_queryset().first()
            answersets = AnswerSet.objects.filter(participant=participant)
            context['single'] = True
            messages = {}
            messages["Participant "+str(participant.location)] = True
            for a in answersets:
                print("AnswerSet ID="+str(a.id)+" on "+str(a.dateAnswered))
                for answer in Answer.objects.filter(answerset=a.id):
                    question = answer.question
                    message = ""
                    if question.style == 0:
                        message += (" "+str(question)+"="+str(answer.scale_Answer))
                    if question.style == 1:
                        message += (" "+str(question)+"="+str(answer.dateFrom))
                    if question.style == 2:
                        message += (" "+str(question)+"="+str(answer.freeform_text))
                    #answers[str(question.id)] = message
                    messages[message] = True
            context['messages'] = messages
        else:
            print("PARTICIPANT LIST")
            messages = {}
            for participant in self.get_queryset():
                if participant.trackingKey:
                    messages["/covid19/dashboard/participant/"+participant.trackingKey] = True
        context['messages'] = messages
        
        return context
