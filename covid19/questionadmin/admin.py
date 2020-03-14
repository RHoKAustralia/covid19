from django.contrib import admin

# Register your models here.
from .models import Question, QuestionType
admin.site.register(Question)
admin.site.register(QuestionType)
