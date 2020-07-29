from django.shortcuts import render

# Create your views here.

def index(request):
  context = {
    "name": "Jatin Katyal",
    "designation": "Senior Software Developer",
    "cv": "https://cb.lk/jatincv"
  }
  return render(request, 'main/index.html', context)