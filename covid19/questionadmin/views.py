from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView
from .forms import ScaleForm
from .forms import QuestionnaireForm
from datetime import datetime

from .models import Question
from .models import Participant
from .models import Answer

class IndexView(generic.ListView):
    context_object_name = 'questions'
    def get_queryset(self):
        return Question.objects.order_by('order')


class ScaleView(generic.FormView):
    template_name = 'questionadmin/question_detail.html'
    form_class = ScaleForm
    success_url = '/handlescale/'

    def form_valid(self, form):
        print("hello")
        return super().form_valid(form)

class QuestionnaireView(generic.FormView):
    template_name = 'questionadmin/question_list.html'
    form_class = QuestionnaireForm
    def asint(valuestr):
        if valuestr=="Yes":
            return 1
        if valuestr=="No":
            return 0
        value = -1
        try:
            value = int(valuestr)
        except:
            value = -1
        return value

    def home(request):
        print("process form")
        if request.method == 'POST':
            print("its a post="+str(request.POST))
            for field in request.POST.keys():
                if field!="csrfmiddlewaretoken":
                    print(str(Question.objects.filter(id=field))+"="+request.POST[field])
            form = QuestionnaireForm(request.POST)
            if form.is_valid():
                pass  # does nothing, just trigger the validation
            # Add the response to the database!
            participant = Participant.objects.all()[:1][0]
            for field in request.POST.keys():
                if field!="csrfmiddlewaretoken":
                    print(str(Question.objects.filter(id=field))+"="+request.POST[field])
                    question = Question.objects.filter(id=field).first()
                    scale_Answer = QuestionnaireView.asint(request.POST[field])
                    answer = Answer(participant=participant,question=question, scale_Answer=scale_Answer,dateAnswered=datetime.now())
                    answer.save()
        else:
            print("its a get")
            form = QuestionnaireForm()
        return render(request, 'bye-page.html')
