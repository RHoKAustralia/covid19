from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.TextField(blank=True, null=True)


class Location(models.Model):
    name = models.TextField(blank=True)


class Participant(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    location = models.ForeignKey('Location')


class Answer(models.Model):
    question = models.ForeignKey('Question')
    participant = models.ForeignKey('Participant')
    scale_Answer = models.IntegerField()
    dateFrom = models.DateTimeField()
    dateTo = models.DateTimeField()
    freeform_text = models.TextField()
