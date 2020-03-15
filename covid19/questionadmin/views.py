from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView
from .forms import ScaleForm

from .models import Question

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

