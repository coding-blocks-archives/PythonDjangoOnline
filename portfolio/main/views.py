from django.shortcuts import render
from django.conf import settings

# Create your views here.

def index(request):
  context = {
    "name": settings.DATA["NAME"],
    "about_me": settings.DATA["ABOUT_ME"]
  }
  return render(request, 'main/index.html', context)

def projects(request):
  context = {
    "projects": settings.DATA["PROJECTS"]
  }
  return render(request, 'main/projects.html', context)

def languages(request):
  context = {
    "languages": settings.DATA["LANGUAGES"]
  }
  return render(request, 'main/languages.html', context)