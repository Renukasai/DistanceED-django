# Generated by Django 4.2.6 on 2023-11-17 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappF23', '0006_remove_course_student_course_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='student',
        ),
        migrations.AddField(
            model_name='course',
            name='interested_students',
            field=models.ManyToManyField(blank=True, to='myappF23.student'),
        ),
    ]
