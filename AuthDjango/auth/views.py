from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.views import LoginView, LogoutView

from auth import forms

# Create your views here.

class Login(LoginView):
  template_name = 'auth/login.html'
  redirect_authenticated_user = True

class Logout(LogoutView):
  pass

def login(request):
  loginForm = forms.LoginForm()
  error = None

  if request.method == "POST":
    loginForm = forms.LoginForm(request.POST)
    if loginForm.is_valid():
      username = loginForm.cleaned_data['username']
      password = loginForm.cleaned_data['password']
      user = authenticate(username = username, password = password, request=request)
      if user:
        auth_login(request, user)
        return HttpResponseRedirect('/')
      else:
        error = "Invalid username or password"

  context = {
    "form": loginForm,
    "error": error
  }
  return render(request, 'auth/login.html', context)
