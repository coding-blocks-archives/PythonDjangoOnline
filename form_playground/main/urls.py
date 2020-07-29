from django.urls import path
from main import views

urlpatterns = [
  path('', views.index),
  path('students', views.students),
  path('addstudent', views.addstudent),
]