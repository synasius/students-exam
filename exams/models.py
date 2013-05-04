__author__ = 'Emanuele Palazzetti <emanuele.palazzetti@gmail.com>'

from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __unicode__(self):
        return self.name


class Course(models.Model):
    COURSE_TYPE_CHOICES = (
        (0, 'Full course'),
        (1, 'Laboratory'),
    )

    name = models.CharField(max_length=200, null=False)
    type = models.IntegerField(choices=COURSE_TYPE_CHOICES, default=0)
    credits = models.IntegerField(default=0)
    department = models.ForeignKey(Department, related_name="courses")

    def __unicode__(self):
        return self.name


class Student(AbstractUser):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length=2, choices=GENDER, default='M')
    exams = models.ManyToManyField(Course, through='Exam')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __unicode__(self):
        return u"{} {}".format(self.first_name, self.last_name)


class Exam(models.Model):
    LAUDE_CHOICES = (
        (0, 'NO'),
        (1, 'YES'),
    )

    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    registration_date = models.DateField('Registration date', null=False, default=datetime.now())
    vote = models.IntegerField(default=0)
    laude = models.IntegerField(default=0, choices=LAUDE_CHOICES)
    note = models.CharField(max_length=200)

    def __unicode__(self):
        return u"{}, {}".format(self.registration_date, self.student)
