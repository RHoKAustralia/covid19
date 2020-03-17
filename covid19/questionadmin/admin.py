from django.contrib import admin

# Register your models here.
from .models import Question, QuestionType, Jurisdiction, HealthWarningTrigger, HealthWarningMessage
from .models import AnswerSet, Answer, Participant
admin.site.register(Question)
admin.site.register(QuestionType)
admin.site.register(Jurisdiction)
admin.site.register(HealthWarningTrigger)
admin.site.register(HealthWarningMessage)
admin.site.register(AnswerSet)
admin.site.register(Answer)
admin.site.register(Participant)
