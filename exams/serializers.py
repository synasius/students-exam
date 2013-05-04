__author__ = 'Emanuele Palazzetti <emanuele.palazzetti@gmail.com>'

from rest_framework import serializers
from exams.models import Department


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'name')
