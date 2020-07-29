from django.http import HttpResponseRedirect
from django.shortcuts import render

from main import (
  forms,
  models
)

# Create your views here.

def index(request):
  context = {
    "form": forms.ExampleForm
  }
  return render(request, 'index.html', context)

def students(request):
  students = models.Student.objects.all()

  context = {
    "students": students
  }
  return render(request, 'students.html', context)

def addstudent(request):
  studentform = forms.StudentForm()

  if request.method == "POST":
    studentform = forms.StudentForm(request.POST)
    if studentform.is_valid():
      student = studentform.save()
      return HttpResponseRedirect('/students')

  context = {
    "studentform": studentform
  }
  return render(request, 'addstudent.html', context)