from django.urls import path
from auth import views

urlpatterns = [
  path('login/', views.Login.as_view()),
  path('logout/', views.Logout.as_view()),
  path('signup/', views.Signup.as_view())
]
