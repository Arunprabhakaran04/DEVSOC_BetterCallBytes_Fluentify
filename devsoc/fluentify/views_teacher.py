from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Student_Credentials as SCreds
from .models import Teacher_Credentials as TCreds
from .models import Classes,Course,Reviews
from . import views
from . import views_login
from django.conf import settings
from django.core.mail import send_mail

def dashboard(request):
    global classes_sch
    template = loader.get_template('teacher_dashboard.html')
    ip = views.get_ip(request)
    # classes_sch = Classes.objects.all().values()
    try:
        nam = views_login.dets()[ip][0]
        ID = views_login.dets()[ip][1]
    except KeyError:
        return HttpResponseRedirect('/')
    Acc_Details = TCreds.objects.get(teacher_id=ID)
    content = {
        'Acc' : Acc_Details,
    }
    return HttpResponse(template.render(content,request))

def add_course(request):
    template = loader.get_template('add_course.html')
    ip = views.get_ip(request)
    try:
        name = views_login.dets()[ip][0]
    except KeyError:
        return HttpResponseRedirect('/')
    
    content = {}
    return HttpResponse(template.render(content,request))

def add_course_process(request):
    return

def add_class(request):
    template = loader.get_template('add_class.html')
    ip = views.get_ip(request)
    try:
        name = views_login.dets()[ip][0]
    except KeyError:
        return HttpResponseRedirect('/')
    
    content = {}
    return HttpResponse(template.render(content,request))

def add_class_process(request):
    ip = views.get_ip(request)
    Lang = request.POST['']
    Pr = request.POST['']
    Tim = request.POST['']
    Dt = request.POST['']
    Teach = views_login.dets()[ip][0]
    classes_ = Classes(Language=Lang,Price=Pr,Timing=Tim,Class_Date=Dt,Teacher=Teach)
    classes_.save()
    return HttpResponseRedirect('/teacher/dashboard/')
