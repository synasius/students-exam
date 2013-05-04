__author__ = 'Emanuele Palazzetti <emanuele.palazzetti@gmail.com>'

from django.contrib import admin
from models import Department, Student, Course, Exam

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Exam)