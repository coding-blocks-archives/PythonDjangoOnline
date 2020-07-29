from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
  developed_by = "Vibhu Dujari"
  mentors = [
    "Prateek Narang",
    "Arnav Gupta",
    "Jatin Katyal",
    "Garima",
    "Anuj Garg"
  ]
  show_developer = False

  context = {
    "developer": developed_by,
    "mentors": mentors,
    "show_developer": show_developer
  }

  response = render(request, 'HelloWorld/index.html', context)
  return response

def hello(request):
  return render(request, 'HelloWorld/hello.html')
