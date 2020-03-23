from django.db import models

# Create your models here.

style_score=0
style_date=1
style_text=2
class Question(models.Model):
    question = models.TextField(blank=True, null=True)
    questiontype = models.ForeignKey('QuestionType', models.DO_NOTHING)
    alias = models.CharField(max_length=50, unique=True, null=True)
    style = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    reportorder = models.IntegerField(default=0)

    class Meta:
        ordering = ('order', 'questiontype')

    def __str__(self):
        return self.question

    # Style
    def isyesno(self):
        if self.istested and str(question)=="Answer":
            return True
        if self.islongterm:
            return True
        return False
    def isanswer(self):
        if str(self.question)=="Answer":
            return True
        return False
    # Groups
    def istested(self):
        if (str(self.questiontype) == "Tested"):
            return True
        return False

    def isscale(self):
        if (str(self.questiontype) == "Scale"):
            return True
        return False

    def isdifficulty(self):
        if (str(self.questiontype) == "Difficulty"):
            return True
        return False

    def istravel(self):
        if (str(self.questiontype) == "Travel"):
            return True
        return False

    def isgathering(self):
        if (str(self.questiontype) == "Gather"):
            return True
        return False

    def iscontact(self):
        if (str(self.questiontype) == "Contact"):
            return True
        return False

    def isisolating(self):
        if (str(self.questiontype) == "Isolating"):
            return True
        return False

    def isage(self):
        if (str(self.questiontype) == "Age"):
            return True
        return False

    def iscountry(self):
        if (str(self.questiontype) == "Country"):
            return True
        return False

    def istown(self):
        if (str(self.questiontype) == "Town"):
            return True
        return False

    def isregion(self):
        if (str(self.questiontype) == "Region"):
            return True
        return False

    def ispostcode(self):
        if (str(self.questiontype) == "Postcode"):
            return True
        return False

    def islongterm(self):
        if (str(self.questiontype) == "Longterm"):
            return True
        return False

    def isaboutyou(self):
        if (str(self.questiontype) == "AboutYou"):
            return True
        return False

    def isflu(self):
        if (str(self.questiontype) == "Influenza"):
            return True
        return False

class QuestionType(models.Model):
    type = models.TextField()

    def __str__(self):
        return self.type

class Location(models.Model):
    place = models.TextField(blank=True)
    postcode = models.TextField(blank=True)
    region = models.ForeignKey('Region', models.DO_NOTHING)
    country = models.ForeignKey('Country', models.DO_NOTHING)
    def __str__(self):
        return str(self.region)+" "+str(self.country)

class Participant(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    location = models.ForeignKey('ParticipantLocation', models.DO_NOTHING)
    age = models.ForeignKey('AgeRanges', models.DO_NOTHING)
    trackingKey = models.CharField(max_length=50, unique=True, null=True)

    @staticmethod
    def generateTrackingKey(request):
        from base64 import b64encode
        import os
        ran_bytes = os.urandom(64)
        token = b64encode(ran_bytes).decode('latin1')[0:6].upper()
        return token

class ParticipantLocation(models.Model):
    # what's the point of this field?
    #participant_id = models.ForeignKey('Participant', models.DO_NOTHING)
    location = models.ForeignKey('Location', models.DO_NOTHING)
    dateFrom = models.DateTimeField(auto_now=True)
    dateTo = models.DateTimeField(auto_now=True)
    #what's the point of this field?
    #current_location= models.BooleanField()
    def __str__(self):
        return str(self.location)

class AnswerSet(models.Model):
    participant = models.ForeignKey('Participant', models.DO_NOTHING)
    dateAnswered = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.participant)+" on "+self.dateAnswered.strftime("%d-%b-%Y (%H:%M:%S.%f)")

class Answer(models.Model):
    question = models.ForeignKey('Question', models.DO_NOTHING)
    participant = models.ForeignKey('Participant', models.DO_NOTHING) # don't need this anymore
    answerset = models.ForeignKey('AnswerSet', models.DO_NOTHING, null=True)
    scale_Answer = models.IntegerField(null=True)
    dateAnswered = models.DateTimeField(null=True) # don't need this anymore
    dateFrom = models.DateTimeField(null=True)
    dateTo = models.DateTimeField(null=True)
    freeform_text = models.TextField(null=True)

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
    def __str__(self):
        return self.country

class Region(models.Model):
    region = models.TextField()
    country = models.ForeignKey('Country', models.DO_NOTHING)
    def __str__(self):
        return self.region+" "+str(self.country)

class AgeRanges(models.Model):
    age_ranges = models.TextField()
    def __str__(self):
        return self.age_ranges

class EmploymentStatus(models.Model):
    status = models.TextField()
    def __str__(self):
        return self.status

class Jurisdiction(models.Model):
    name = models.TextField()

class HealthWarningTrigger(models.Model):
    jurisdiction = models.ForeignKey('Jurisdiction', models.DO_NOTHING)
    question = models.ForeignKey('Question', models.DO_NOTHING)
    warninglevel = models.IntegerField(null=True)
    warningadvice = models.TextField()
    mininclusive = models.IntegerField(null=True)
    maxinclusive = models.IntegerField(null=True)

class HealthWarningMessage(models.Model):
    warninglevel = models.IntegerField(null=True)
    warningadvice = models.TextField()
    def __str__(self):
        return self.warningadvice
