from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.TextField(blank=True, null=True)
    questiontype = models.ForeignKey('Questiontype')

class Questiontype(models.Model):
    type = models.TextField()

class Location(models.Model):
    place = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    region = models.ForeignKey('Region')
    country = models.ForeignKey('Country')

class Participant(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    location = models.ForeignKey('Participant_location')
    age = models.ForeignKey('AgeRanges')

class Participant_location(models.Model):
    participant = models.ForeignKey('Participant')
    location = models.ForeignKey('Location')
    dateFrom = models.DateTimeField()
    dateTo = models.DateTimeField()
    current_location= models.Boolean()

class Answer(models.Model):
    question = models.ForeignKey('Question')
    participant = models.ForeignKey('Participant')
    scale_Answer = models.IntegerField()
    dateFrom = models.DateTimeField()
    dateTo = models.DateTimeField()
    freeform_text = models.TextField()

class  Health(models.Model):
    participant = models.ForeignKey('Participant')
    issue = models.ForeignKey('GlobalHealthSchema')
    severity = models.IntegerField()

class GlobalHealthSchema(models.Model):
    medical_term  = models.TextField()
    common_term = models.TextField()
    external_classification_code = models.TextField()

class Event(models.Model):
    participant = models.ForeignKey('Participant')
    name = models.TextField()
    location = models.ForeignKey('Participant_location')

class Contacts(models.Model):
    participant = models.ForeignKey('Participant')
    location = models.ForeignKey('Participant_location')

class Country(models.Model):
    country = models.TextField()
    international_country_code = models.TextField()

class Region(models.Model):
    region = models.TextField()
    country = models.ForeignKey('Country')

class AgeRanges(models.Model):
    age_ranges = models.TextField()
