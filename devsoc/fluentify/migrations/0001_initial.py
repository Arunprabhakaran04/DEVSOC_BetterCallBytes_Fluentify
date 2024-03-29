# Generated by Django 4.1 on 2024-03-17 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('Students', models.CharField(auto_created=True, default='0', max_length=255)),
                ('Class_Date', models.CharField(auto_created=True, default=datetime.date(2024, 3, 17), max_length=255)),
                ('CLASS_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('Language', models.CharField(default='-', max_length=255)),
                ('Price', models.CharField(default='0', max_length=255)),
                ('Timing', models.CharField(default='-', max_length=255)),
                ('Teacher', models.CharField(default='-', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Credentials',
            fields=[
                ('notes', models.CharField(auto_created=True, default='', max_length=2000)),
                ('status', models.CharField(auto_created=True, default='Active', max_length=50)),
                ('student_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(default='Not Given', max_length=255)),
                ('phone', models.CharField(default='Not Given', max_length=50)),
                ('u_id', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(default='1234', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('Teacher_ID', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('Language', models.CharField(default='-', max_length=255)),
                ('Proficiency', models.CharField(default='Elementry', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_Credentials',
            fields=[
                ('status', models.CharField(auto_created=True, default='Active', max_length=50)),
                ('teacher_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(default='Not Given', max_length=255)),
                ('phone', models.CharField(default='Not Given', max_length=50)),
                ('u_id', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(default='1234', max_length=255)),
            ],
        ),
    ]
