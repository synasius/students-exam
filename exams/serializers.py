__author__ = 'Emanuele Palazzetti <emanuele.palazzetti@gmail.com>'

from rest_framework import serializers
from exams.models import Department, Course, Student, Exam


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course


class ExamSerializer(serializers.ModelSerializer):
    course = serializers.RelatedField(read_only=True)
    student = serializers.RelatedField(read_only=True)

    class Meta:
        model = Exam


class StudentSerializer(serializers.ModelSerializer):
    exams = ExamSerializer(many=True)

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'gender', 'exams')
