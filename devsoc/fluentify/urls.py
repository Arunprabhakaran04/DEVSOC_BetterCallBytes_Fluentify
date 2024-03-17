from django.urls import path,include
from . import views
from . import views_login as log
from . import views_teacher as teacher
from . import views_student as student
from django.conf import settings
from django.conf.urls.static import static


#For UI output
urlpatterns = [
    path('',log.login,name='login'),
    path('register/',log.register,name='register'),
    path('register/process/',log.process_register,name='register_process'),
    path('register/process/',log.process_register,name='process'),
    path('logout/',log.logout,name='logout'),

    #Student URLS
    path('student/',log.student_login,name="Student_login"),
    path('student/login_check/',log.login_check_student,name='student_check'),
    path('student/register/',log.register,name='register'),
    path('student/register/process/',log.process_register,name='register_process'),
    path('student/dashboard/',student.dashboard,name="Student_Dashboard"),
    path('student/dashboard/logout/',log.logout,name='logout'),
    path('student/dashboard/show_courses/',student.show_courses,name="Courses"),

    #Teacher URLS
    path('teacher/',log.teacher_login,name="Teacher_login"),
    path('teacher/login_check/',log.login_check_teacher,name='teacher_check'),
    path('teacher/register/',log.register,name='register'),
    path('teacher/register/process/',log.process_register,name='register_process'),
    # path('teacher/register_edit/<str:u_id>',log.edit_register_student,name='student_regedit'),
    # path('teacher/register_edit/done/<str:u_id>',log.edit_register_process_student,name='student_regedit_process'),
    path('teacher/dashboard/add_review/<str:TID>',student.add_review,name="Add Review"),
    path('teacher/dashboard/add_review/process/',student.add_review_process,name="Add Review Process"),
    path('teacher/dashboard/',teacher.dashboard,name="Teacher_Dashboard"),
    path('teacher/dashboard/logout/',log.logout,name='logout'),
    path('teacher/dashboard/show_course/',teacher.show_courses,name="Show_Courses"),
    path('teacher/dashboard/add_course/',teacher.add_course,name="Add Course"),
    path('teacher/dashboard/add_course/process/',teacher.add_course_process,name="Add_Course_Process"),
    path('teacher/dashboard/add_class/',teacher.add_class,name="Add_Class"),
    path('teacher/dashboard/add_class/process/',teacher.add_class_process,name="Add Class Process"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
