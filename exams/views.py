__author__ = 'Emanuele Palazzetti <emanuele.palazzetti@gmail.com>'

from rest_framework import generics

from exams.models import Department
from exams.serializers import DepartmentSerializer


class DepartmentList(generics.ListCreateAPIView):
    model = Department
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Department
    serializer_class = DepartmentSerializer
