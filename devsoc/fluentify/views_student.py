from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Student_Credentials as SCreds
from .models import Teacher_Credentials as TCreds
from .models import Classes,Course,Reviews
from . import views
from . import views_login
from . import views_teacher
from django.conf import settings
from django.core.mail import send_mail


def dashboard(request):
    template = loader.get_template('student_dashboard.html')
    ip = views.get_ip(request)
    try:
        user = views_login.dets()[ip][0]
        ID = views_login.dets()[ip][1]

    except KeyError:
        return HttpResponseRedirect('/')
    Acc_Details = SCreds.objects.get(student_id=ID)

    content = {
        'Acc' : Acc_Details,

    }
    return HttpResponse(template.render(content,request))

def show_courses(request):
    template = loader.get_template('show_courses.html')
    ip = views.get_ip(request)
    try:
        name = views_login.dets()[ip][0]
    except KeyError:
        return HttpResponseRedirect('/')
    courses = Course.objects.all().values()
    content = {
        'courses' : courses,
    }
    return HttpResponse(template.render(content,request))

def add_review(request,TID):
    template = loader.get_template('add_review.html')
    ip = views.get_ip(request)
    try:
        name = views_login.dets()[ip][0]
    except KeyError:
        return HttpResponseRedirect('/')
    content = {
        'TID' : TID,
    }
    return HttpResponse(template.render(content,request))

def add_review_process(request):
    ip = views.get_ip(request)
    try:
        ID = views_login.dets()[ip][1]
    except KeyError:
        return HttpResponseRedirect('/')
    TID = request.POST['TID']
    rating = request.POST['rating']
    review = request.POST['review']
    review_ = Reviews(Student_ID=ID,Teacher_ID=TID,Rating=rating,Review=review)
    review_.save()
    return HttpResponseRedirect('/student/dashboard/my_courses/')