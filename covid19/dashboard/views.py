from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView

from questionadmin.models import Question

# Create your views here.
class IndexView(generic.ListView):
    context_object_name = 'questions'
    def get_queryset(self):
        print("do the queryset\n")
        return Question.objects.order_by('order')
    def get_template(self):
        return 'dashboard/question_list.html'
    def index(request):
        print("do the index\n")
        latest_question_list = Question.objects.order_by('order')
        context = {'questions': latest_question_list}
        return render(request, 'dashboard/question_list.html', context)

