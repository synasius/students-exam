__author__ = 'Emanuele Palazzetti <emanuele.palazzetti@gmail.com>'

from rest_framework import generics

from exams.models import Department, Course, Student, Exam
from exams.serializers import DepartmentSerializer, CourseSerializer, StudentSerializer, ExamSerializer


class DepartmentList(generics.ListCreateAPIView):
    model = Department
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Department
    serializer_class = DepartmentSerializer


class CourseList(generics.ListCreateAPIView):
    model = Course
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Course
    serializer_class = CourseSerializer


class StudentList(generics.ListCreateAPIView):
    model = Student
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Student
    serializer_class = StudentSerializer


class ExamList(generics.ListCreateAPIView):
    model = Exam
    serializer_class = ExamSerializer


class ExamDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Exam
    serializer_class = ExamSerializer
