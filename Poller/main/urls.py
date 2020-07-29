from django.urls import path
from django.contrib.auth.decorators import login_required

from main import views

urlpatterns = [
  path('', views.Index.as_view(), name = 'index'),
  path('question/<slug>', login_required(views.Question.as_view()), name = 'question')
]
