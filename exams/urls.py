__author__ = 'Emanuele Palazzetti <emanuele.palazzetti@gmail.com>'

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from exams import views


urlpatterns = patterns('',
   url(r'^department/$', views.DepartmentList.as_view()),
   url(r'^department/(?P<pk>[0-9]+)/$', views.DepartmentDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)