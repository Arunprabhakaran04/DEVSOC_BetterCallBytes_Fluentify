from django.db import models
from datetime import datetime,date

# Create your models here.
class Teacher_Credentials(models.Model):
    name = models.CharField(max_length=255,blank=False)
    teacher_id = models.AutoField(blank=False,unique=True,primary_key=True,auto_created=True)
    email = models.CharField(max_length=255,default='Not Given')
    phone = models.CharField(max_length=50,default='Not Given',blank=False)
    u_id = models.CharField(max_length=255,unique=True,blank=False)
    password = models.CharField(max_length=255,default='1234')
    status = models.CharField(max_length=50,default='Active',auto_created=True,blank=False)


class Student_Credentials(models.Model):
    name = models.CharField(max_length=255,blank=False)
    student_id = models.AutoField(blank=False,unique=True,primary_key=True,auto_created=True)
    email = models.CharField(max_length=255,default='Not Given')
    phone = models.CharField(max_length=50,default='Not Given',blank=False)
    u_id = models.CharField(max_length=255,unique=True,blank=False)
    password = models.CharField(max_length=255,default='1234')
    status = models.CharField(max_length=50,default='Active',auto_created=True,blank=False)
    notes = models.CharField(max_length=2000,default="",auto_created=True,blank=False)

class Classes(models.Model):
    Course_ID = models.CharField(max_length=255,blank=False,default="-")
    CLASS_ID = models.AutoField(blank=False,unique=True,primary_key=True,auto_created=True)
    # Language = models.CharField(max_length=255,blank=False,default="-")
    #Price = models.CharField(max_length=255,blank=False,default="0")
    Timing = models.CharField(max_length=255,blank=False,default="-")
    Class_Date = models.CharField(max_length=255,blank=False,default=date.today(),auto_created=True)
    # Teacher = models.CharField(max_length=255,blank=False,default="-")
    # Students = models.CharField(max_length=255,blank=False,default="0",auto_created=True)

class Course(models.Model):
    Course_ID = models.AutoField(blank=False,unique=True,primary_key=True,auto_created=True)
    Course_name = models.CharField(max_length=255,blank=False,default="-")
    Teacher_ID = models.CharField(max_length=255,blank=False,unique=True)
    Language = models.CharField(max_length=255,blank=False,default="-")
    Proficiency = models.CharField(max_length=255,blank=False,default="Elementry")
    Price = models.CharField(max_length=255,blank=False,default="0")
    Students = models.IntegerField(blank=False,default=0,auto_created=True)

class Reviews(models.Model):
    Review_ID = models.AutoField(blank=False,unique=True,primary_key=True,auto_created=True)
    Student_ID = models.CharField(max_length=255,blank=False)
    Teacher_ID = models.CharField(max_length=255,blank=False)
    Rating = models.CharField(max_length=255,blank=False,default="3")
    Review = models.CharField(max_length=255,blank=False,default="-") 

