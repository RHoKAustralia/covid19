from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView
from .forms import ScaleForm
from .forms import QuestionnaireForm
from datetime import datetime
import pytz
from pytz import timezone

from .models import Question
from .models import Location
from .models import Country
from .models import ParticipantLocation
from .models import Participant
from .models import Answer
from .models import AnswerSet
from .models import HealthWarningTrigger
from .models import HealthWarningMessage
from .models import AgeRanges
from .models import EmploymentStatus
from .models import Region

    #
countryList = [
	"Afghanistan",
	"Albania",
	"Algeria",
	"American Samoa",
	"Andorra",
	"Angola",
	"Anguilla",
	"Antarctica",
	"Antigua and Barbuda",
	"Argentina",
	"Armenia",
	"Aruba",
	"Australia",
	"Austria",
	"Azerbaijan",
	"Bahamas (the)",
	"Bahrain",
	"Bangladesh",
	"Barbados",
	"Belarus",
	"Belgium",
	"Belize",
	"Benin",
	"Bermuda",
	"Bhutan",
	"Bolivia (Plurinational State of)",
	"Bonaire, Sint Eustatius and Saba",
	"Bosnia and Herzegovina",
	"Botswana",
	"Bouvet Island",
	"Brazil",
	"British Indian Ocean Territory (the)",
	"Brunei Darussalam",
	"Bulgaria",
	"Burkina Faso",
	"Burundi",
	"Cabo Verde",
	"Cambodia",
	"Cameroon",
	"Canada",
	"Cayman Islands (the)",
	"Central African Republic (the)",
	"Chad",
	"Chile",
	"China",
	"Christmas Island",
	"Cocos (Keeling) Islands (the)",
	"Colombia",
	"Comoros (the)",
	"Congo (the Democratic Republic of the)",
	"Congo (the)",
	"Cook Islands (the)",
	"Costa Rica",
	"Croatia",
	"Cuba",
	"Curaçao",
	"Cyprus",
	"Czechia",
	"Côte d'Ivoire",
	"Denmark",
	"Djibouti",
	"Dominica",
	"Dominican Republic (the)",
	"Ecuador",
	"Egypt",
	"El Salvador",
	"Equatorial Guinea",
	"Eritrea",
	"Estonia",
	"Eswatini",
	"Ethiopia",
	"Falkland Islands (the) [Malvinas]",
	"Faroe Islands (the)",
	"Fiji",
	"Finland",
	"France",
	"French Guiana",
	"French Polynesia",
	"French Southern Territories (the)",
	"Gabon",
	"Gambia (the)",
	"Georgia",
	"Germany",
	"Ghana",
	"Gibraltar",
	"Greece",
	"Greenland",
	"Grenada",
	"Guadeloupe",
	"Guam",
	"Guatemala",
	"Guernsey",
	"Guinea",
	"Guinea-Bissau",
	"Guyana",
	"Haiti",
	"Heard Island and McDonald Islands",
	"Holy See (the)",
	"Honduras",
	"Hong Kong",
	"Hungary",
	"Iceland",
	"India",
	"Indonesia",
	"Iran (Islamic Republic of)",
	"Iraq",
	"Ireland",
	"Isle of Man",
	"Israel",
	"Italy",
	"Jamaica",
	"Japan",
	"Jersey",
	"Jordan",
	"Kazakhstan",
	"Kenya",
	"Kiribati",
	"Korea (the Democratic People's Republic of)",
	"Korea (the Republic of)",
	"Kuwait",
	"Kyrgyzstan",
	"Lao People's Democratic Republic (the)",
	"Latvia",
	"Lebanon",
	"Lesotho",
	"Liberia",
	"Libya",
	"Liechtenstein",
	"Lithuania",
	"Luxembourg",
	"Macao",
	"Madagascar",
	"Malawi",
	"Malaysia",
	"Maldives",
	"Mali",
	"Malta",
	"Marshall Islands (the)",
	"Martinique",
	"Mauritania",
	"Mauritius",
	"Mayotte",
	"Mexico",
	"Micronesia (Federated States of)",
	"Moldova (the Republic of)",
	"Monaco",
	"Mongolia",
	"Montenegro",
	"Montserrat",
	"Morocco",
	"Mozambique",
	"Myanmar",
	"Namibia",
	"Nauru",
	"Nepal",
	"Netherlands (the)",
	"New Caledonia",
	"New Zealand",
	"Nicaragua",
	"Niger (the)",
	"Nigeria",
	"Niue",
	"Norfolk Island",
	"Northern Mariana Islands (the)",
	"Norway",
	"Oman",
	"Pakistan",
	"Palau",
	"Palestine, State of",
	"Panama",
	"Papua New Guinea",
	"Paraguay",
	"Peru",
	"Philippines (the)",
	"Pitcairn",
	"Poland",
	"Portugal",
	"Puerto Rico",
	"Qatar",
	"Republic of North Macedonia",
	"Romania",
	"Russian Federation (the)",
	"Rwanda",
	"Réunion",
	"Saint Barthélemy",
	"Saint Helena, Ascension and Tristan da Cunha",
	"Saint Kitts and Nevis",
	"Saint Lucia",
	"Saint Martin (French part)",
	"Saint Pierre and Miquelon",
	"Saint Vincent and the Grenadines",
	"Samoa",
	"San Marino",
	"Sao Tome and Principe",
	"Saudi Arabia",
	"Senegal",
	"Serbia",
	"Seychelles",
	"Sierra Leone",
	"Singapore",
	"Sint Maarten (Dutch part)",
	"Slovakia",
	"Slovenia",
	"Solomon Islands",
	"Somalia",
	"South Africa",
	"South Georgia and the South Sandwich Islands",
	"South Sudan",
	"Spain",
	"Sri Lanka",
	"Sudan (the)",
	"Suriname",
	"Svalbard and Jan Mayen",
	"Sweden",
	"Switzerland",
	"Syrian Arab Republic",
	"Taiwan (Province of China)",
	"Tajikistan",
	"Tanzania, United Republic of",
	"Thailand",
	"Timor-Leste",
	"Togo",
	"Tokelau",
	"Tonga",
	"Trinidad and Tobago",
	"Tunisia",
	"Turkey",
	"Turkmenistan",
	"Turks and Caicos Islands (the)",
	"Tuvalu",
	"Uganda",
	"Ukraine",
	"United Arab Emirates (the)",
	"United Kingdom of Great Britain and Northern Ireland (the)",
	"United States Minor Outlying Islands (the)",
	"United States of America (the)",
	"Uruguay",
	"Uzbekistan",
	"Vanuatu",
	"Venezuela (Bolivarian Republic of)",
	"Viet Nam",
	"Virgin Islands (British)",
	"Virgin Islands (U.S.)",
	"Wallis and Futuna",
	"Western Sahara",
	"Yemen",
	"Zambia",
	"Zimbabwe",
	"Åland Islands"
]

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

class IndexView(generic.ListView):
    context_object_name = 'questions'
    #
    def get_queryset(self):
        return Question.objects.order_by('order')

    def get_context_data(self,**kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context["countryList"] = countryList
        print("return custom context")
        return context

class TrackedView(generic.ListView):
    context_object_name = 'questions'
    #
    def get_queryset(self):
        return Question.objects.order_by('order')

    def get_context_data(self,**kwargs):
        context = super(TrackedView,self).get_context_data(**kwargs)
        context["countryList"] = countryList
        context["generatedKey"] = Participant.generateTrackingKey(self.request)
        context["tracked"] = True
        print("return custom context")
        return context



class ScaleView(generic.FormView):
    template_name = 'questionadmin/question_detail.html'
    form_class = ScaleForm
    success_url = '/handlescale/'

    def form_valid(self, form):
        print("hello")
        return super().form_valid(form)

class QuestionnaireView(generic.FormView):
    template_name = 'questionadmin/question_list.html'
    form_class = QuestionnaireForm
    def asint(valuestr):
        if valuestr=="Yes":
            return 1
        if valuestr=="No":
            return 0
        value = -1
        try:
            value = int(valuestr)
        except:
            value = -1
        return value

    def asdate(valuestr):
        from dateutil import parser
        # ds = '2012-03-01T10:00:00Z' # or any date sting of differing formats.
        try:
            value = parser.parse(valuestr)
        except:
            value = None
        return value

    def astext(valuestr):
        value = valuestr
        return value

    def nowUTC():
        return datetime.now(timezone('UTC'))

    def findGenderAsInteger(request):
        expected_question = Question.objects.filter(alias="sex").first()
        user_response = request.POST[str(expected_question.id)] # the users response value
        value = -1
        if user_response == "Female":
            value = 1
        elif user_response == "Male":
            value = 2
        elif user_response == "Other":
            value = 3
        return value

    def findAgeRange(request):
        # Foreign key
        expected_question = Question.objects.filter(alias="age").first() # the AgeRange question
        user_response = request.POST[str(expected_question.id)] # the users response value
        value = AgeRanges.objects.filter(age_ranges=user_response).first()
        if not value:
            value = AgeRanges.objects.all().first()
            if not value:
               value = AgeRanges(age_ranges="unknown")
        return value

    def findEmploymentStatus(request):
        # Foreign key
        expected_question = Question.objects.filter(alias="employment").first() # the AgeRange question
        user_reponse = request.POST[str(expected_question.id)] # the users response value
        value = EmploymentStatus.objects.filter(status=user_reponse).first()
        if not value:
            value = EmploymentStatus.objects.all().first()
            if not value:
               value = EmploymentStatus(status="unknown")
        return value

    def findTrackingKey(request):
        value = None
        for field in request.POST.keys():
            if str(field)=="uid":
                value = request.POST[field]
        print("UID="+str(value))
        return value

    def findCountry(request):
        # Foreign key
        expected_question = Question.objects.filter(questiontype__type="Country").first() # the question
        user_reponse = request.POST[str(expected_question.id)] # the users response value
        value = Country.objects.filter(country=user_reponse).first()
        if not value:
            value = Country.objects.all().first()
            if not value:
               value = Country(country="unknown",international_country_code="unkown")
        return value

    def findPlace(request):
        # Text
        expected_question = Question.objects.filter(questiontype__type="Town").first() # the question
        user_reponse = request.POST[str(expected_question.id)] # the users response value
        value = user_reponse

    def findPostcode(request):
        # Text
        expected_question = Question.objects.filter(questiontype__type="Postcode").first() # the AgeRange question
        return request.POST[str(expected_question.id)] # the users response value

    def findRegion(request):
        # Foreign key
        expected_question = Question.objects.filter(questiontype__type="Country").first() # the question
        user_reponse = request.POST[str(expected_question.id)] # the users response value
        value = Region.objects.filter(region=user_reponse).first()
        if not value:
            value = Region.objects.all().first()
            if not value:
               value = Region(region="unknown",country="unkown")
        return value

    def home(request):
        print("process form")
        myset = {}
        if request.method == 'POST':
            #print("its a post="+str(request.POST))
            #print("AGE RANGE ID"+str(QuestionnaireView.findAgeRange(request)))
            form = QuestionnaireForm(request.POST)
            if form.is_valid():
                pass  # does nothing, just trigger the validation
            # Add the response to the database!
            # look for participant
            # if not found create one with firstName, lastName, [location], [agerange], trackingKey
            firstName = "anon" # no way to pass it
            lastName = "anon" # no way to pass it
            # look for location
            place = QuestionnaireView.findPlace(request)
            postcode = QuestionnaireView.findPostcode(request)
            region = QuestionnaireView.findRegion(request)
            country = QuestionnaireView.findCountry(request)
            print("USER LOCATION="+str(place)+" "+str(postcode)+" "+str(region)+" "+str(country))
            #found_place = Region.filter(region=region)
            #found_region = Region.filter(region=region)
            location = Location.objects.filter(country__country=country).filter(region=region).first()
            print("location="+str(location))
            # if not found create one with place,postcode,[region],[country]
             
            location = Location.objects.all().first() # any location for now
            age = AgeRanges.objects.filter(age_ranges=QuestionnaireView.findAgeRange(request)).first()
            if not age:
                age = AgeRanges.objects.all().first()
            trackingKey = QuestionnaireView.findTrackingKey(request) # still need to pass it
            participantlocation = ParticipantLocation.objects.all().first() # any participant location
            participant = None
            if trackingKey:
                print("UID PASSED="+str(trackingKey))
                participant = Participant.objects.filter(trackingKey=trackingKey).first()
            if not participant:
                print("Create New Participant="+str(trackingKey))
                participant = Participant(firstName=firstName,lastName=lastName,location=participantlocation,age=age, trackingKey=trackingKey)
            participant.save()
            answerset = AnswerSet(participant=participant, dateAnswered=QuestionnaireView.nowUTC())
            answerset.save()
            for field in request.POST.keys():
                print(".field="+str(field))
                if field!="csrfmiddlewaretoken" and is_number(field):
                    question = Question.objects.filter(id=field).first()
                    #print("Question="+str(question)+" "+str(request.POST[field]))
                    if question.style == 0:
                        # scale
                        if str(question.alias) == "age":
                            scale_Answer = QuestionnaireView.findAgeRange(request).id
                        elif str(question.alias)=="sex":
                            scale_Answer = QuestionnaireView.findGenderAsInteger(request)
                        elif str(question.alias)=="employment":
                            scale_Answer = QuestionnaireView.findEmploymentStatus(request).id
                        else:
                            scale_Answer = QuestionnaireView.asint(request.POST[field])
                        answer = Answer(participant=participant,question=question, scale_Answer=scale_Answer,dateAnswered=QuestionnaireView.nowUTC(),
                                        answerset=answerset)
                        myset[question.id] = scale_Answer
                    if question.style == 1:
                        # datetime
                        date_Answer = QuestionnaireView.asdate(request.POST[field])
                        answer = Answer(participant=participant,question=question, dateFrom=date_Answer,dateAnswered=QuestionnaireView.nowUTC(),
                                        answerset=answerset)
                    if question.style == 2:
                        # text
                        text_Answer = QuestionnaireView.astext(request.POST[field])
                        answer = Answer(participant=participant,question=question, freeform_text=text_Answer,dateAnswered=QuestionnaireView.nowUTC(),
                                        answerset=answerset)
                        
                    answer.save()
                elif field!="csrfmiddlewaretoken":
                    question = Question.objects.filter(question=field).first()
                    if question:
                        text_Answer = QuestionnaireView.astext(request.POST[field])
                        answer = Answer(participant=participant,question=question, freeform_text=text_Answer,dateAnswered=QuestionnaireView.nowUTC(),
                                        answerset=answerset)

                    answer.save()

        else:
            print("its a get")
            form = QuestionnaireForm()
        print("DONE")

        # stub for working out the health warning message
        level = 0
        jurisdictionid = 1
        for q in myset.keys():
            triggers = HealthWarningTrigger.objects.filter(question=q)
            for i in triggers:
                print("trigger="+str(triggers[:1][0]))
                if myset[q] >= triggers[:1][0].mininclusive and myset[q] <= triggers[:1][0].maxinclusive:
                    level += triggers[:1][0].warninglevel
        message = HealthWarningMessage.objects.filter(warninglevel=0).first()
        for i in range(level,0,-1):
           print("check "+str(i)+" size="+str(HealthWarningMessage.objects.filter(warninglevel=i).count()))
           if HealthWarningMessage.objects.filter(warninglevel=i).count() > 0:
              message = HealthWarningMessage.objects.filter(warninglevel=i).first()
              break
        context = {
            'level':level,
            'message':message,
        }
        return render(request, 'bye-page.html',context)

