from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.TextField(blank=True, null=True)
    questiontype = models.ForeignKey('QuestionType', models.DO_NOTHING)

class QuestionType(models.Model):
    type = models.TextField()

class Location(models.Model):
    place = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    region = models.ForeignKey('Region', models.DO_NOTHING)
    country = models.ForeignKey('Country', models.DO_NOTHING)

class Participant(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    location = models.ForeignKey('ParticipantLocation', models.DO_NOTHING)
    age = models.ForeignKey('AgeRanges', models.DO_NOTHING)

class ParticipantLocation(models.Model):
    participant_id = models.ForeignKey('Participant', models.DO_NOTHING)
    location = models.ForeignKey('Location', models.DO_NOTHING)
    dateFrom = models.DateTimeField()
    dateTo = models.DateTimeField()
    current_location= models.BooleanField()

class Answer(models.Model):
    question = models.ForeignKey('Question', models.DO_NOTHING)
    participant = models.ForeignKey('Participant', models.DO_NOTHING)
    scale_Answer = models.IntegerField()
    dateFrom = models.DateTimeField()
    dateTo = models.DateTimeField()
    freeform_text = models.TextField()

class  Health(models.Model):
    participant = models.ForeignKey('Participant', models.DO_NOTHING)
    issue = models.ForeignKey('GlobalHealthSchema', models.DO_NOTHING)
    severity = models.IntegerField()

class GlobalHealthSchema(models.Model):
    medical_term  = models.TextField()
    common_term = models.TextField()
    external_classification_code = models.TextField()

class Event(models.Model):
    participant = models.ForeignKey('Participant', models.DO_NOTHING)
    name = models.TextField()
    location = models.ForeignKey('ParticipantLocation', models.DO_NOTHING)

class Contacts(models.Model):
    participant = models.ForeignKey('Participant', models.DO_NOTHING)
    location = models.ForeignKey('ParticipantLocation', models.DO_NOTHING)

class Country(models.Model):
    country = models.TextField()
    international_country_code = models.TextField()

class Region(models.Model):
    region = models.TextField()
    country = models.ForeignKey('Country', models.DO_NOTHING)

class AgeRanges(models.Model):
    age_ranges = models.TextField()
