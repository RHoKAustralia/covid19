from django.contrib import admin

# Register your models here.
from .models import Question, QuestionType, Jurisdiction, HealthWarningTrigger, HealthWarningMessage
admin.site.register(Question)
admin.site.register(QuestionType)
admin.site.register(Jurisdiction)
admin.site.register(HealthWarningTrigger)
admin.site.register(HealthWarningMessage)
