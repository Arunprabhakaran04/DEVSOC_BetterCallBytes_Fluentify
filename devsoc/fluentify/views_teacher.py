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
    ip = views.get_ip(request)
    try:
        ID = views_login.dets()[ip][1]
    except KeyError:
        return HttpResponseRedirect('/')
    
    Coursename = request.POST['']
    Lang = request.POST['']
    Prof = request.POST['']
    Price = request.POST['']
    course_ = Course(Course_name=Coursename,Teacher_ID=ID,Language=Lang,Proficiency=Prof,Price=Price)
    course_.save()
    Courseid = Course.objects.get(Course_name=Coursename,Teacher_ID=ID).Course_ID
    no = request.POST['']
    for i in range(0,no):
        Tim = request.POST['']
        Dt = request.POST['']
        classes_ = Classes(Timing=Tim,Class_Date=Dt,Course_ID=Courseid)
        classes_.save()
    return HttpResponseRedirect('/teacher/dashboard/')
def course_details(request):
    template = loader.get_template('course_details.html')
    ip = views.get_ip(request)
    try:
        ID = views_login.dets()[ip][1]
    except KeyError:
        return HttpResponseRedirect('/')
    teacher_courses = Course.objects.all().filter(Teacher_ID=ID).values()
    content = {
        'courses' : teacher_courses,
    }
    return HttpResponse(template.render(content,request))

# def add_class(request):
#     template = loader.get_template('add_class.html')
#     ip = views.get_ip(request)
#     try:
#         name = views_login.dets()[ip][0]
#     except KeyError:
#         return HttpResponseRedirect('/')
    
#     content = {}
#     return HttpResponse(template.render(content,request))

# def add_class_process(request):
#     ip = views.get_ip(request)
#     try:
#         name = views_login.dets()[ip][0]
#     except KeyError:
#         return HttpResponseRedirect('/')
    
#     Courseid = request.POST['']
#     Tim = request.POST['']
#     Dt = request.POST['']
#     classes_ = Classes(Timing=Tim,Class_Date=Dt,Course_ID=Courseid)
#     classes_.save()
#     return HttpResponseRedirect('/teacher/dashboard/')

def show_courses(request):
    template = loader.get_template('show_courses_tutor.html')
    ip = views.get_ip(request)
    try:
        ID = views_login.dets()[ip][1]
    except KeyError:
        return HttpResponseRedirect('/')
    
    content = {}
    return HttpResponse(template.render(content,request))

