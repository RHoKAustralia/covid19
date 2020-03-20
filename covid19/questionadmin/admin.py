from django.contrib import admin

# Register your models here.
from .models import Question, QuestionType, Jurisdiction, HealthWarningTrigger, HealthWarningMessage
from .models import AnswerSet, Answer, Participant, AgeRanges, Location, ParticipantLocation, Health, Contacts
from .models import GlobalHealthSchema, Event, Country, Region, EmploymentStatus
admin.site.register(Question)
admin.site.register(QuestionType)
admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(ParticipantLocation)
admin.site.register(AnswerSet)
admin.site.register(Answer)
admin.site.register(Health)
admin.site.register(GlobalHealthSchema)
admin.site.register(Event)
admin.site.register(Contacts)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(AgeRanges)
admin.site.register(EmploymentStatus)
admin.site.register(Jurisdiction)
admin.site.register(HealthWarningTrigger)
admin.site.register(HealthWarningMessage)

