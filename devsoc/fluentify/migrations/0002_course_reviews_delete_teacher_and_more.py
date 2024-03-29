# Generated by Django 4.1 on 2024-03-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fluentify', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Students', models.CharField(auto_created=True, default='0', max_length=255)),
                ('Course_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('Course_name', models.CharField(default='-', max_length=255)),
                ('Teacher_ID', models.CharField(max_length=255, unique=True)),
                ('Language', models.CharField(default='-', max_length=255)),
                ('Proficiency', models.CharField(default='Elementry', max_length=255)),
                ('Price', models.CharField(default='0', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('Review_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('Student_ID', models.CharField(max_length=255)),
                ('Teacher_ID', models.CharField(max_length=255)),
                ('Rating', models.CharField(default='3', max_length=255)),
                ('Review', models.CharField(default='-', max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='Language',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='Students',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='Teacher',
        ),
        migrations.AddField(
            model_name='classes',
            name='Course_ID',
            field=models.CharField(default='-', max_length=255),
        ),
    ]
