from django.http  import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


class Person(object):

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


def greeting(request): #firts view

    p1 = Person("Gabriel", "Guerra")


    #name = "Gabriel"
    #last_name = "Guerra"

    subject_of_course = ["Template", "Models", "Forms", "Views", "Deployment"]

    now = datetime.datetime.now()

    #doc_extern = open("C:/Users/jgabr/Desktop/project_django/project_django/templates/1-template.html")

    #plt = Template(doc_extern.read())

    #doc_extern.close()

    #doc_extern = get_template('1-template.html')

    #ctx = Context({"name_person" : p1.name, "lastname_person": p1.last_name, "moment_now": now,
    #"Subject": subject_of_course})

    #document = doc_extern.render({"name_person" : p1.name, "lastname_person": p1.last_name, "moment_now": now,
    #"Subject": subject_of_course})

    #return HttpResponse(document)
    return render(request, "1-template.html", {"name_person" : p1.name, "lastname_person": p1.last_name, "moment_now": now,
    "Subject": subject_of_course})

def courseC(request):
    date_now = datetime.datetime.now()

    return render(request, "CourseC.html", {"givemedate": date_now})


def courseCss(request):
    date_now = datetime.datetime.now()

    return render(request, "courseCss.html", {"givemedate": date_now})

def goodbye(request):
    return HttpResponse("Good Bye")


def givemedate(request):
    date_now = datetime.datetime.now()

    document = """
    <html>
    <body>
    <h2>
    Date and time now %s
    </h2>
    </body>
    </html>

    """% date_now

    return HttpResponse(document)

def calculateAge(request, age, year):
    #yearNow = 18
    period = year - 2019
    ageFuture = age + period
    document= "<html><body><h2>In the year %s your have %s years</html></body></h2>"%(year, ageFuture)

    return HttpResponse(document)
