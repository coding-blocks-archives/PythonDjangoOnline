from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  return render(request, 'main/index.html')

@login_required(login_url='/auth/login')
def sshh(request):
  return HttpResponse("This is a authenticated view !")
