from django.urls import path

from main import views

urlpatterns = [
  path('', views.Index.as_view())
]
